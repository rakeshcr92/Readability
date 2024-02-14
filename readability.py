#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def find_letters(text):
    """Count the number of letters in the text."""
    letters = "abcdefghijklmnopqrstuvwxyz "
    return sum(1 for char in text if char.lower() in letters)

def find_words(text):
    """Count the number of words in the text."""
    return len(text.split())

def find_sentences(text):
    """Count the number of sentences in the text."""
    sentence_breakers = ['.', '?', '!', '—']
    return sum(1 for char in text if char in sentence_breakers)

def calculate_grade_level(text):
    """
    Calculate the approximate grade level needed to comprehend the text
    using the Coleman-Liau index formula.
    """
    n_letters = find_letters(text)
    n_sentences = find_sentences(text)
    n_words = find_words(text)

    L = (n_letters / n_words) * 100
    S = (n_sentences / n_words) * 100

    grade_level = round(0.0588 * L - 0.296 * S - 15.8)
    return grade_level

def main():
    """Main function to get input from the user and display the grade level."""
    text = input("Enter text for readability evaluation: ").strip()
    
    if not text:
        print("Error: Please enter some text.")
        return

    grade_level = calculate_grade_level(text)
    print(f"Grade level: {grade_level}")

if __name__ == "__main__":
    main()

