# -*- coding: utf-8 -*-
__author__ = 'zym'
import math
import string
import jieba
import re

def get_distance(doc1,doc2):
    word_dict1=word_frequency_of_text(doc1)
    word_dict2=word_frequency_of_text(doc2)
    distance=vector_angle(word_dict1,word_dict2)
    return distance

def word_frequency_of_text(text):
    text=pre_process(text)
    words=get_words_from_text(text)
    freq_mapping=count_frequency(words)
    return freq_mapping

def get_words_from_text(text):
    words=list(jieba.cut(text))
    return words

def count_frequency(words):
    word_dict={}
    for word in words:
        word_dict[word]=word_dict.get(word,0)+1
    return word_dict

def inner_product(D1,D2):
    """
    Inner product between two vectors, where vectors
    are represented as dictionaries of (word,freq) pairs.
    Example: inner_product({"and":3,"of":2,"the":5},
                           {"and":4,"in":1,"of":1,"this":2}) = 14.0
    """
    sum=0.0
    for key in D1:
        if key in D2:
            sum+=D1[key]*D2[key]
    return sum

def vector_angle(D1,D2):
    numerator=inner_product(D1,D2)
    denominator=math.sqrt(inner_product(D1,D1)*inner_product(D2,D2))
    return 1-numerator/denominator

def pre_process(text):
    text=re.sub(ur"[\n\r ]","",text)
    return text