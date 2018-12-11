import string

path = r'E:\学习\python\Walden.txt'

with open(path, 'rb') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in str(text.read().split())]
    words_index = set(words)
    counts_dict = {index:words.count(index) for index in words_index}

for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
    print('{} - {} times'.format(word,counts_dict[word]))