import string

def count_words(filename):
    word_count = {}
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.lower().translate(str.maketrans('', '', string.punctuation))
                words = line.split()
                
                for word in words:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return
    sorted_word_count = dict(sorted(word_count.items()))
    for word, count in sorted_word_count.items():
        print(f"{word}: {count}")
filename = input("Enter the filename to count words: ")
count_words(filename)
