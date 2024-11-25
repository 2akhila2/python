
def get_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in word.lower() if char in vowels]
    return result
word = input("Enter a word: ")
vowel_list = get_vowels(word)
print(f"The vowels in the word '{word}' are: {vowel_list}")

