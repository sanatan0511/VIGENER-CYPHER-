# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:08:27 2024

@author: rashm
"""

import string
from collections import Counter


def frequency_analysis(text):
    frequency = {letter: 0 for letter in string.ascii_uppercase}
    for letter in text:
        if letter.upper() in frequency:
            frequency[letter.upper()] += 1
    return frequency


def read_encrypted_file(file_path):
    with open(file_path, 'r') as file:
        encrypted_text = file.read()
    return encrypted_text


def segment_frequency_analysis(text, key_length):
    segments = [''.join([text[i] for i in range(j, len(text), key_length)]) for j in range(key_length)]
    segment_frequencies = [frequency_analysis(segment) for segment in segments]
    return segment_frequencies


def print_segment_frequency_analysis(segment_frequencies):
    for i, freq in enumerate(segment_frequencies):
        print(f"Frequency Analysis for Segment {i + 1}:")
        for letter, count in sorted(freq.items()):
            print(f"{letter}: {count}")
        print()


file_path = "C:/Users/rashm/Downloads/encrypted_vignere (2).txt"


encrypted_text = read_encrypted_file(file_path)


clean_text = ''.join(filter(str.isalpha, encrypted_text)).upper()


key_length = 4
segment_frequencies = segment_frequency_analysis(clean_text, key_length)


print_segment_frequency_analysis(segment_frequencies)
