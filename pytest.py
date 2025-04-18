import re
from collections import Counter

def most_frequent_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    counts = Counter(words)
    return counts.most_common(1)[0][0]

print(most_frequent_word("This is a test. This test is only a test."))
