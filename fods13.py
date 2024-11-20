from collections import Counter
with open('sample_text.txt', 'r') as file:
    text = file.read()
words = text.lower().split()
word_freq = Counter(words)
print("Word frequency distribution:\n", word_freq)
