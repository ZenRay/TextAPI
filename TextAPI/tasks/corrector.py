#coding:utf8
"""
This module provides guard whether the text contains wrong words. `pycorrector`
is the basis.
"""
from __future__ import absolute_import

import pycorrector

from collections import defaultdict
from ..config import CONFUSION_PATH

__all__ = ["text_corrector"]
def text_corrector(text, confusion:bool=True, non_level="char"):
    """Correct Text

    Check text whether contains wrong word. If `confusion` is True, add 
    customize confusion words(can add more words, file path is 
    `config/ConfusionWords.txt`) that is a file path. Word level can use `char`, 
    `word` or None, `char` is character level which can check single wrong word; 
    None is can't support single word level

    Parameters:
    @type bool, confusion, whether add confusion word
    @type string, non_level, choose a level, `char` close character level, `word`
        close word level. None can support the two level

    Results:
    @type dict, result, wrong words, and those start index

    Examples:
    >>> text_corrector('少先队员因该为老人让坐') # add confusion and use char level
        defaultdict(dict, {0: {'word': '因该', 'start_index': 4}})
    >>> # add confusion and use all level
    >>> text_corrector('少先队员因该为老人让坐', non_level=None)
        {'因该': 4, '坐': 10}
    """
    # add confusion dict
    if confusion:
        pycorrector.set_custom_confusion_dict(CONFUSION_PATH)

    # import ipdb; ipdb.set_trace() 
    # get wrong word information
    report = pycorrector.detect(text)
    if len(report) > 0:
        result = defaultdict(dict)
    else:
        return 

    for index, item in enumerate(report):
        if non_level is None:
            result[index]["word"] = item[0]
            result[index]["start_index"] = item[1]
        elif non_level == "char" and len(item[0]) > 1:
            result[index]["word"] = item[0]
            result[index]["start_index"] = item[1]
        elif non_level == "word" and len(item[0]) == 1:
            result[index]["word"] = item[0]
            result[index]["start_index"] = item[1] 

    return result