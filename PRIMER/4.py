#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    file = open("file2.txt", "r")
    content = file.readlines()
    print(content)
    file.close()