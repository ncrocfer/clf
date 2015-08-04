# -*- coding: utf-8 -*-

"""
This module contains functions that are used in CLF.
"""

import requests
import os
from lxml import html
import yaml

from clf.constants import URL
from clf.exceptions import RequestsException, OSException, DuplicateException
from clf.command import Command


def get_snippet(id, proxies):
    url = '{}/commands/view/{}'.format(URL, id)

    try:
        r = requests.get(url, proxies=proxies)
    except requests.exceptions.ConnectionError:
        raise RequestsException("The connection is not available")

    if url not in r.url:
        raise RequestsException("The snippet does not seem to exist.")

    tree = html.fromstring(r.text)

    c = Command(id,
                str(tree.xpath('//div[@class="command"]/text()')[0]),
                str(tree.xpath('//div[@id="terminal-header"]/h1/text()')[0]),
                str(tree.xpath('//div[@class="num-votes"]/text()')[0]),
                str(r.url)
    )

    return c


def save_snippet(id, proxies):
    snippets_file = get_snippets_file()

    with open(snippets_file, 'r') as f:
        data = yaml.load(f)

        if id not in data:
            snippet = get_snippet(id, proxies)
            data[id] = snippet

            with open(snippets_file, 'w') as f:
                yaml.dump(data, f)
        else:
            raise DuplicateException('The snippet is already saved.')

    return snippet


def get_snippets_file():
    snippets_file = os.path.join(os.path.expanduser('~'), '.clf.yaml')

    if not os.path.isfile(snippets_file):
        try:
            f = open(snippets_file, 'w')
            f.close()
        except OSError:
            raise OSException('Could not create {}'.format(snippets_file))

    return snippets_file


def get_local_snippets():
    snippets_file = get_snippets_file()

    with open(snippets_file, 'r') as f:
        data = yaml.load(f)

    return data.values()