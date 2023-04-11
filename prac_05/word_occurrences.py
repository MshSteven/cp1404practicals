"""
Word Occurrences
Estimate: 20 minutes
Actual:   13 minutes
"""
input_text = input("Text: ")
words = list(input_text.split())
words.sort()
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

max_length = max(len(word) for word in list(word_to_count.keys()))
for word, count in word_to_count.items():
    print(f"{word:{max_length}} : {count}")
