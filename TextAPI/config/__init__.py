#coding:utf8
from __future__ import absolute_import
from os import path

# Load Sensitive Words
with open(path.join(path.dirname(__file__), "SC_Taboo.txt"), "r") as file:
    TABOO = set(word.strip() for word in file.readlines())

# Load Corrector Confusion words, refere:
#  https://github.com/shibing624/pycorrector/blob/master/examples/use_custom_confusion.py
CONFUSION_PATH = path.join(path.dirname(__file__), "ConfusionWords.txt")

__all__ = ["TABOO", "CONFUSION_PATH"]