# 2.Write a Python program to read a text file and count the number of words in it.
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count=len(words)
        return word_count
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return 0

file_path ="C:\\Users\\jayja\\Desktop\\vsec practice\\sample.txt" 
total_words = count_words_in_file(file_path)

print("Total number of words in given file are:",total_words)