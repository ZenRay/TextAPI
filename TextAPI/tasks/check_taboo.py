#coding:utf8
"""Check Taboo Word

This module provides guard whether the text contains taboo words. Jieba
segment is the basis:
* Firstly, separate the word from the text
* Secondly, check whether the word is taboo
"""
from __future__ import absolute_import

import jieba
import re
from TextAPI.config import TABOO

# Add addictive words
for word in TABOO:
    jieba.add_word(word)


def taboo_stamp(text):
    words = [word for word in jieba.cut(text) if word in TABOO]
    if len(words) > 0:
        result = {
            "taboo_status": True,
            "words": words
        }
        return result
    else:
        return {
            "taboo_status": False,
            "words": []
        }


def taboo_stamp2(text):
    """Regex Check Taboo"""
    result = {
            "taboo_status": False,
            "words": []
        }
    for word in TABOO:
        pattern = re.compile(word, re.I)
        if bool(pattern.search(text)):
            result["words"].append(word)
            result["taboo_status"] = True
    
    return result