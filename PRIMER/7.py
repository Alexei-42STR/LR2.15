#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    fp = open('file2.txt', 'r')
    print("The filepointer is at byte :", fp.tell())
    content = fp.read();
    print("After reading, the filepointer is at:", fp.tell())