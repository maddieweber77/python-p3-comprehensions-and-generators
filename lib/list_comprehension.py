#!/usr/bin/env python3

def return_evens(num_list):
    even_nums=[]
    for i in num_list:
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums




def make_exclamation(sentence_list):
    excited_sentences = []
    for i in sentence_list:
        if i != "":
            excited_sentences.append(f"{i}!")
    return excited_sentences