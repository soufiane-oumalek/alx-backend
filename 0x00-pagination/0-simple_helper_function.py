#!/usr/bin/env python3
""" Simple helper function """


def index_range(page, page_size):
    """  function should return a tuple of size two containing
    a start index and an end index corresponding
    to the range of indexes to return in a list for
    those particular pagination parameters """
    return ((page - 1) * page_size), ((page - 1) * page_size) + page_size
