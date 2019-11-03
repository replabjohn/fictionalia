#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

#use_nltk.py

"""Module collecting our routines for using the Natual Language Toolkit.

Funtion modify_text is currently a stub.

"""

try:
    import nltk
    NlTL_FOUND = 1
except:
    print "NLTKNOT FOUND"
    NlTL_FOUND = 0


def modify_text(text):
    #stub
    return text



if __name__ == "__main__":
    print
    print "use_nltk.py"
    print
    if NlTL_FOUND ==1 :
        print "NLTK found OK."
    else:
        print "NLTK NOT found."
    print
    x = modify_text("Hello World")
    print x
    print
 