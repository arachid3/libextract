"""
    libextract.pruners
    ~~~~~~~~~~~~~~~~~~

<<<<<<< HEAD
For example, if we were to not know that the *text_length* quantifier
existed, we would simply create our own, under the following protocols:

```python
    from libextract.pruners import selects
    from libextract.html._xpaths import NODES_WITH_TEXT

    # INPUTS
    # "node" must declared, selector must be given as keyword argument
    # user must assume it is an lxml.html.HtmlElement object
    @selects(selector=NODES_WITH_TEXT)
    def my_pruner(node):
        text = node.text
        textlen = len(' '.join(text.split())) if text else 0
        return node.getparent(), textlen
    # OUTPUTS
    # lxml.html.HtmlElement, numerical or collections.Counter
```
=======
    Implements functions to aid `pruning`, a phase before
    the prediction of which nodes are the most likely ones
    containing text.
>>>>>>> 113744fb65b31626c94276c90173c8f53e986803
"""

from __future__ import absolute_import
from functools import wraps
from collections import Counter

from libextract.html.xpaths import SELECT_ALL, NODES_WITH_TEXT
from libextract.metrics import count_children, text_length


def selects(selector):
<<<<<<< HEAD
=======
    """
    Given an XPath selector *selector*, returns a function
    that yields the result of calling the wrapped function
    on every node matching the *selector*.
    """
>>>>>>> 113744fb65b31626c94276c90173c8f53e986803
    def decorator(func):
        @wraps(func)
        def quantifier(etree):
            for node in etree.xpath(selector):
                yield func(node)
        return quantifier
    return decorator


<<<<<<< HEAD
@selects(selector=SELECT_ALL)
=======
@selects(SELECT_ALL)
>>>>>>> 113744fb65b31626c94276c90173c8f53e986803
def prune_by_child_count(node):
    """
    Given an *etree*, returns an iterable of parent
    to child node frequencies (collections.Counter) pairs.
    """

    return node, count_children(node) or Counter()


<<<<<<< HEAD
@selects(selector=NODES_WITH_TEXT)
=======
@selects(NODES_WITH_TEXT)
>>>>>>> 113744fb65b31626c94276c90173c8f53e986803
def prune_by_text_length(node):
    """
    Given an *etree*, returns an iterable of parent
    to node text length pairs.
    """
    return node.getparent(), text_length(node)
