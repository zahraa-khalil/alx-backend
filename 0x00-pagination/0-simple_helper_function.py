#!/usr/bin/env python3
"""Pagination Module"""


def index_range(page, page_size):
    """return a tuple of size two"""
    return ((page - 1) * page_size, page * page_size)
