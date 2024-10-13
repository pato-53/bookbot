
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_words(text)
    characters = char_count(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for char, count in characters.items():
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")        



def char_count(text):
    chars_dict = {}
    
    for char in text:
        lowered = char.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    
    sorted_chars = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))

    return sorted_chars


def get_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()