# -*- coding: utf-8 -*-

"""
This module implements the Commandlinefu.com API
"""

import requests
import base64

from clf.command import Command
from clf.constants import URL
from clf.exceptions import (FormatException, OrderException,
                            QueryException, RequestsException)


class Clf(object):

    def __init__(self, format="json", order="votes"):
        if format not in ['json', 'plaintext', 'rss']:
            raise FormatException('The format is invalid')

        self.format = format
        self.url = URL

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

    def get(self, url):
        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError:
            raise RequestsException("The connection is not available")

        return r.json()

    def browse(self):
        commands = self.get(self._prepare_browse_url())
        return self.cmd_generator(commands)

    def command(self, cmd):
        commands = self.get(self._prepare_command_url(cmd))
        return self.cmd_generator(commands)

    def search(self, *args):
        commands = self.get(self._prepare_search_url(*args))
        return self.cmd_generator(commands)

    def cmd_generator(self, commands):
        for command in commands:
            yield Command(
                command['id'],
                command['command'],
                command['summary'],
                command['votes'],
                command['url']
            )
