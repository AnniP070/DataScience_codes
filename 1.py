# 1.Write a Python program to count the frequency of each word in a given string using a dictionary.
def count_word_freq(str):
    word_count = {}
    words = str.lower().split()
    for i in words:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1
    return word_count

sample_string = "Hello, hello world! This is a test. Hello world."
result = count_word_freq(sample_string)

for word, count in result.items():
    print(word,":",count)
    
