# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

def counting_vowels_and_consonants(text_entry):
    number_vowels = 0
    number_consonants = 0
    for letter in text_entry: 
        if letter in "AaEeIiOoUu":
            number_vowels += 1
        elif letter.isalpha(): 
            number_consonants += 1
    return (number_vowels, number_consonants)

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(text_entry):
    number_of_sentences = 0
    for letter in text_entry:
        if letter in ".?!":
            number_of_sentences += 1
    for letter in text_entry:
        total_vowels, total_consonants = counting_vowels_and_consonants(text_entry)
    avg_vowels = total_vowels / number_of_sentences 
    avg_consonants = total_consonants / number_of_sentences
    return (number_of_sentences, avg_vowels, avg_consonants)
text_entry = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

print(f"the result of the avergae vowels, consonants, and sentences, with text_entry equal to some quotes is {average_vowels_and_consonants(text_entry)}")