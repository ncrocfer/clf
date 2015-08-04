# -*- coding: utf-8 -*-

"""
This module contains the list of clf exceptions
"""


class FormatException(Exception):
    """ The format is invalid """


class OrderException(Exception):
    """ The order is invalid """


class QueryException(Exception):
    """ The parameter is invalid """


class RequestsException(Exception):
    """ The request is invalid """


class OSException(Exception):
    """ An OS error has occurred """


class DuplicateException(Exception):
    """ The snippet already exists """
