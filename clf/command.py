# -*- coding: utf-8 -*-

"""
This class contains the class on which all the commands will be based
"""


class Command(object):

    def __init__(self, id, command, summary, votes, url):
        self.id = id
        self.command = command
        self.summary = summary
        self.votes = votes
        self.url = url

    def __repr__(self):
        return "{}(id={}, command={}, summary={}, votes={}, url={})".format(
            self.__class__.__name__,
            self.id,
            self.command,
            self.summary,
            self.votes,
            self.url
        )
