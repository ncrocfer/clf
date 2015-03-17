#!/usr/bin/env python

"""
All the tests for CLF are here
"""


import types
import unittest
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

from clf.api import Clf
from clf.command import Command
from clf.constants import URL
from clf.exceptions import (FormatException, OrderException,
                            QueryException)


class ClfTestCase(unittest.TestCase):

    def setUp(self):
        self.urls = {
            'browse_by_votes_in_json': '/commands/browse/sort-by-votes/json',
            'browse_by_votes_in_xml': '/commands/browse/sort-by-votes/xml',
            'browse_by_votes_in_plaintext': '/commands/browse/'
                                            'sort-by-votes/plaintext',
            'browse_by_date_in_json': '/commands/browse//json',
            'browse_by_date_in_xml': '/commands/browse//xml',
            'browse_by_date_in_plaintext': '/commands/browse//plaintext',
            'command_by_votes_in_json': '/commands/using/tar/'
                                        'sort-by-votes/json',
            'command_by_votes_in_xml': '/commands/using/tar/sort-by-votes/xml',
            'command_by_votes_in_plaintext': '/commands/using/tar/'
                                             'sort-by-votes/plaintext',
            'command_by_date_in_json': '/commands/using/tar//json',
            'command_by_date_in_xml': '/commands/using/tar//xml',
            'command_by_date_in_plaintext': '/commands/using/tar//plaintext',
            'search_by_votes_in_json': '/commands/matching/'
                                       'python-server/cHl0aG9uIHNlcnZlcg==/'
                                       'sort-by-votes/json',
            'search_by_votes_in_xml': '/commands/matching/'
                                      'python-server/cHl0aG9uIHNlcnZlcg==/'
                                      'sort-by-votes/xml',
            'search_by_votes_in_plaintext': '/commands/matching/'
                                            'python-server/'
                                            'cHl0aG9uIHNlcnZlcg==/'
                                            'sort-by-votes/plaintext',
            'search_by_date_in_json': '/commands/matching/python-server/'
                                      'cHl0aG9uIHNlcnZlcg==//json',
            'search_by_date_in_xml': '/commands/matching/python-server/'
                                     'cHl0aG9uIHNlcnZlcg==//xml',
            'search_by_date_in_plaintext': '/commands/matching/python-server/'
                                           'cHl0aG9uIHNlcnZlcg==//plaintext',

        }
        self.urls = {k: urljoin(URL, v) for k, v in self.urls.items()}

    def tearDown(self):
        pass

    def test_browse_urls(self):
        for order in ['votes', 'date']:
            clf = Clf(order=order)

            for format in ['json', 'xml', 'plaintext']:
                clf.format = format
                url = self.urls['browse_by_' + order + '_in_' + format]
                self.assertEqual(clf._prepare_browse_url(),
                                 url)

    def test_command_urls(self):
        for order in ['votes', 'date']:
            clf = Clf(order=order)

            for format in ['json', 'xml', 'plaintext']:
                clf.format = format
                url = self.urls['command_by_' + order + '_in_' + format]
                self.assertEqual(clf._prepare_command_url('tar'),
                                 url)

    def test_search_urls(self):
        for order in ['votes', 'date']:
            clf = Clf(order=order)

            for format in ['json', 'xml', 'plaintext']:
                clf.format = format

                url = self.urls['search_by_' + order + '_in_' + format]
                self.assertEqual(clf._prepare_search_url('python server'),
                                 url)
                self.assertEqual(clf._prepare_search_url(['python', 'server']),
                                 url)

    def test_browse(self):
        commands = Clf().browse()
        self.assertIsInstance(commands, types.GeneratorType)
        self.assertIsInstance(next(commands), Command)
        self.assertEqual(24, sum(1 for _ in commands))

    def test_command(self):
        commands = Clf().command('tar')
        self.assertIsInstance(commands, types.GeneratorType)
        self.assertIsInstance(next(commands), Command)
        self.assertEqual(24, sum(1 for _ in commands))

    def test_search(self):
        commands = Clf().search('python server')
        self.assertIsInstance(commands, types.GeneratorType)
        self.assertIsInstance(next(commands), Command)
        self.assertGreater(sum(1 for _ in commands), 0)

    def test_exceptions(self):
        with self.assertRaises(FormatException):
            Clf(format='foo')

        with self.assertRaises(OrderException):
            Clf(order='foo')

        with self.assertRaises(QueryException):
            Clf()._prepare_search_url({'foo': 'bar'})


if __name__ == '__main__':
    unittest.main()
