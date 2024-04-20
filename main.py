def main():
    book_path = "books/frankenstein.txt"
    full_text = get_text_string(book_path)
    word_count = get_word_count(full_text)
    count_letter = get_count_letters(full_text)
    print_report(book_path, word_count, count_letter)
    

def get_text_string(path):
    with open(path) as f:
        return f.read()
    

def get_word_count(text):
    text_splt = text.split()
    return len(text_splt)

def get_count_letters(text):
    letter_count = dict()
    for i in text:
        if i.isalpha():
            lower_letter = i.lower()
            if lower_letter in letter_count:
                letter_count[lower_letter] = letter_count[lower_letter] + 1
            else:
                letter_count[lower_letter] = 1
    return dict(sorted(letter_count.items(),reverse=True, key=lambda item: item[1]))

def print_report(book_path, word_count, count_letter):
    print(f"### Begin Text Report of {book_path} ###\n")
    print(f"There are {word_count} words found in the book")

    for letter in count_letter:
        print(f"'{letter}' was found {count_letter[letter]} times")

    print("\n### End of Report ###")

    
main()