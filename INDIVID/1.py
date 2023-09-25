#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 7. Написать программу, которая считывает текст из файла и определяет, сколько в нем слов, состоящих из не менее чем семи букв.

if __name__ == '__main__':
with open('text.txt', 'r') as f:
text = f.read()
text = text.replace("!", ".")
text = text.replace("?", ".")
while ".." in text:
text = text.replace("..", ".")
sentences = text.split(".")
for sentence in sentences:
if "," in sentence:
print(sentence)
