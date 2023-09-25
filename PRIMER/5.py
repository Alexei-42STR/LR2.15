#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    file = open("newfile1.txt", "x")
    print(file)
    if file:
        print("File created successfully")
    file.close()