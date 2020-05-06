#coding:utf8
"""Check Taboo Word

This module provides guard whether the text contains taboo words. Jieba
segment is the basis:
* Firstly, separate the word from the text
* Secondly, check whether the word is taboo
those found in Perl.  It supports both 8-bit and Unicode strings; both
the pattern and the strings being processed can contain null bytes and
characters outside the US ASCII range.

Regular expressions can contain both special and ordinary characters.
Most ordinary characters, like "A", "a", or "0", are the simplest
regular expressions; they simply match themselves.  You can
concatenate ordinary characters, so last matches the string 'last'
"""
from __future__ import absolute_import

import jieba

from TextAPI.config import TABOO

# Add addictive words
for word in TABOO:
    jieba.add_word(word)


def taboo_stamp(text):
    words = [word for word in jieba.cut(text) if word in TABOO]
    if len(words) > 0:
        return True
    else:
        return False