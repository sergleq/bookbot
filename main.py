import sys
from stats import get_num_words
from stats import get_sort_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    raise sys.exit(1)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {get_num_words()} total words")
print("--------- Character Count -------")
for chars in get_sort_list():
    print(f"{chars['char']}: {chars['num']}")
print("============= END ===============")