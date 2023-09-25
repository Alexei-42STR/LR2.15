#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 7. Разработайте программу, которая будет показывать слово (или слова), чаще остальных встречающееся в текстовом файле. Сначала пользователь должен ввести имя файла для обработки. После этого вы должны открыть файл и проанализировать его построчно, разделив при этом строки по словам и исключив из них пробелы и знаки препинания. Также при подсчете частоты появления слов в файле вам стоит игнорировать регистры.
if __name__ == "__main__":
    
s = inf.read().replace('\n', ' ').lower().split()
words = {}
words[s[0]] = 1
k = 0

for i in range (0,len(s)-1):
    if s[i] in words:
        k+=1
        words[s[i]] = k
    else:
        words[s[i]] = 1

word = list(words.keys())
word_count = list(words.values())
max_word_count = 0
min_word = ''

for i in range(len(word_count)-1):
    if  word_count[i] > max_word_count:
        max_word_count = word_count[i]
        min_word = word[i]
        
    elif word_count[i] == max_word_count:
        if word[i] < min_word:
            min_word = word[i]

print(min_word,max_word_count)
