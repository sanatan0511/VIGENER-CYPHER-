
import string
from collections import Counter


def index_of_coincidence(text):
    N = len(text)
    frequency = Counter(text)
    IC = sum(f * (f - 1) for f in frequency.values()) / (N * (N - 1))
    return IC


def guess_key_length(text, max_key_length=20):
    average_IC = []
    for key_length in range(1, max_key_length + 1):
        segments = [''.join([text[i] for i in range(j, len(text), key_length)]) for j in range(key_length)]
        ICs = [index_of_coincidence(segment) for segment in segments]
        average_IC.append(sum(ICs) / len(ICs))
    return average_IC


def read_encrypted_file(file_path):
    with open(file_path, 'r') as file:
        encrypted_text = file.read()
    return encrypted_text


file_path = "C:/Users/rashm/Downloads/encrypted_vignere (2).txt"

# Read the encrypted text
encrypted_text = read_encrypted_file(file_path)

# Clean the text by removing non-alphabetic characters
clean_text = ''.join(filter(str.isalpha, encrypted_text)).upper()

# Guess the key length
average_IC = guess_key_length(clean_text)


print("Average Index of Coincidence for different key lengths:")
for i, ic in enumerate(average_IC, 1):
    print(f"Key Length {i}: {ic:.4f}")


def frequency_analysis(text):
    frequency = {letter: 0 for letter in string.ascii_uppercase}
    for letter in text:
        if letter.upper() in frequency:
            frequency[letter.upper()] += 1
    return frequency


def print_frequency_analysis(frequency):
    print("Frequency Analysis of Encrypted Text:")
    for letter, freq in sorted(frequency.items()):
        print(f"{letter}: {freq}")


frequency = frequency_analysis(clean_text)


print_frequency_analysis(frequency)
