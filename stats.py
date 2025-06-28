import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words():  
    list_words = get_book_text(sys.argv[1]).split()
    return len(list_words)

def get_num_characters():
    char_list = {}
    lower_string = get_book_text(sys.argv[1]).lower()
    for char in lower_string:
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1        
    return char_list

def get_sort_list():
    char_list = []
    char_dict = get_num_characters()
    
    for char in char_dict:
        if char.isalpha():
            entry = {
                "char": char,
                "num": char_dict[char]
            }
            char_list.append(entry)

    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list


