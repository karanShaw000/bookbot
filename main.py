def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_word(text):
    words = text.split()
    return len(words)

def count_characters(text):
    count = {}
    lowercase_text = text.lower()
    for c in lowercase_text:
        if c in count :
            count[c] += 1
        else:
            count[c] = 1

    return count

def sort_count_characters(count_character_dict):
    list_of_letter = []

    # convert dict to list of dict ie array of object
    for letter in count_character_dict:
        if letter.isalpha() :
            list_of_letter.append({ "letter" : letter, "freq": count_character_dict[letter] })

    # Sorting the list wrt to frequency of letter. Here "lambda x: x["freq"] means a function where x is a dict
    # and return dictnary's freq key value
    list_of_letter.sort(reverse=True, key= lambda x : x["freq"])

    return list_of_letter

def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    no_of_words = count_word(text)
    character_count = count_characters(text)
    sorted_character_count = sort_count_characters(character_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{no_of_words} words found in the document")
    print()
    print()
    for i in sorted_character_count:
        letter = i["letter"]
        freq = i["freq"]
        print(f"The '{letter}' character was found {freq} times")

main()
