#coding:utf8
from __future__ import absolute_import
from os import path

# Load Sensitive Words
with open(path.join(path.dirname(__file__), "SC_Taboo.txt"), "r") as file:
    TABOO = set(word.strip() for word in file.readlines())



__all__ = ["TABOO"]