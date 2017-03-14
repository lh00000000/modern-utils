#!/usr/bin/python
# -*- coding: utf-8 -*-
def is_python2():
    try:
        print("💩")
        return False
    except SyntaxError:
        return True
