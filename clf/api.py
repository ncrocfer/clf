# -*- coding: utf-8 -*-

"""
This module implements the Commandlinefu.com API
"""

import requests
import base64

try:
    from urllib import getproxies
except ImportError:
    from urllib.request import getproxies

try:
    from urlparse import urlparse
except ImportError:
    from urllib import parse as urlparse

from clf.command import Command
from clf.constants import URL
from clf.exceptions import (FormatException, OrderException,
                            QueryException, RequestsException)


class Clf(object):

    def __init__(self, format="json", order="votes", proxy=None):
        if format not in ['json', 'plaintext', 'rss']:
            raise FormatException('The format is invalid')

        self.format = format
        self.url = URL
        self.proxy = proxy

        if order == 'votes':
            self.order = 'sort-by-votes'
        elif order == 'date':
            self.order = ''
        else:
            raise OrderException('The order is invalid')

    def _prepare_search_url(self, *args):
        if isinstance(args[0], list):
            query = ' '.join(args[0])
        elif isinstance(args[0], str):
            query = ' '.join(args[0].split())  # remove multiple blanks
        else:
            raise QueryException('The method expects a string or a list')

        b64_query = base64.b64encode(query.encode('utf-8')).decode('utf-8')
        url_query = '-'.join(query.split())

        return "{}/commands/matching/{}/{}/{}/{}".format(self.url,
                                                         url_query,
                                                         b64_query,
                                                         self.order,
                                                         self.format)

    def _prepare_command_url(self, cmd):
        return "{}/commands/using/{}/{}/{}".format(self.url,
                                                   cmd,
                                                   self.order,
                                                   self.format)

    def _prepare_browse_url(self):
        return "{}/commands/browse/{}/{}".format(self.url,
                                                 self.order,
                                                 self.format)

    def _get_proxies(self):
        proxies = getproxies()

        proxy = {}
        if self.proxy:
            parsed_proxy = urlparse(self.proxy)
            proxy[parsed_proxy.scheme] = parsed_proxy.geturl()

        proxies.update(proxy)
        return proxies

    def _get(self, url):
        proxies = self._get_proxies()

        try:
            r = requests.get(url, proxies=proxies)
        except requests.exceptions.ConnectionError:
            raise RequestsException("The connection is not available")

        try:
            return r.json()
        except ValueError:
            return []

    def _cmd_generator(self, commands):
        for command in commands:
            yield Command(
                command['id'],
                command['command'],
                command['summary'],
                command['votes'],
                command['url']
            )

    def browse(self):
        commands = self._get(self._prepare_browse_url())
        return self._cmd_generator(commands)

    def command(self, cmd):
        commands = self._get(self._prepare_command_url(cmd))
        return self._cmd_generator(commands)

    def search(self, *args):
        commands = self._get(self._prepare_search_url(*args))
        return self._cmd_generator(commands)
