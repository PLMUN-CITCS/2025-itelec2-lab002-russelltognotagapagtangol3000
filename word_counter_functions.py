def get_sentence_input() -> str:
    """
    Prompts the user to enter a sentence and returns it as a string.
    """
    return input("Enter a sentence: ").strip()

def count_words(sentence: str) -> int:
    """
    Counts the number of words in the given sentence.
    A word is defined as any sequence of characters separated by spaces.
    
    :param sentence: The input sentence as a string.
    :return: The number of words in the sentence.
    """
    return len(sentence.split())

def main():
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} words.")

if __name__ == "__main__":
    main()