"""
    libextract.pruners
    ~~~~~~~~~~~~~~~~~~

    Implements functions to aid `pruning`, a phase before
    the prediction of which nodes are the most likely ones
    containing text.
"""

from __future__ import absolute_import
from functools import wraps
from collections import Counter

from libextract.html.xpaths import SELECT_ALL, NODES_WITH_TEXT
from libextract.metrics import count_children, text_length


def selects(selector):
    """
    Given an XPath selector *selector*, returns a function
    that yields the result of calling the wrapped function
    on every node matching the *selector*.
    """
    def decorator(func):
        @wraps(func)
        def quantifier(etree):
            for node in etree.xpath(selector):
                yield func(node)
        return quantifier
    return decorator


@selects(SELECT_ALL)
def prune_by_child_count(node):
    """
    Given an *etree*, returns an iterable of parent
    to child node frequencies (collections.Counter) pairs.
    """

    return node, count_children(node) or Counter()


@selects(NODES_WITH_TEXT)
def prune_by_text_length(node):
    """
    Given an *etree*, returns an iterable of parent
    to node text length pairs.
    """
    return node.getparent(), text_length(node)
