from __future__ import absolute_import

from libextract.coretools import argmax


def node_counter_argmax(pairs):
    """
    Return the most frequent pair in a given iterable of
    (node, collections.Counter) *pairs*.
    """
    for node, children in pairs:
        if children:
            yield node, argmax(children)
