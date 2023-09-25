#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 8. В данном упражнении вы должны написать программу, которая будет находить самое
# длинное слово в файле. В качестве результата программа должна выводить на экран длину
# самого длинного слова и все слова такой длины. Для простоты принимайте за значимые
# буквы любые непробельные символы, включая цифры и знаки препинания.

if __name__ == "__main__":

    def longest_word(filename):
        with open("2txt.txt", "r", encoding="utf-8") as infile:
            words = infile.read().split()
        max_len = len(max(words, key=len))
        return [word for word in words if len(word) == max_len]

    print(longest_word("1.txt"))