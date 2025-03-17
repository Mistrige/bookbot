import sys
from stats import(get_num_words, get_letter_count, sorted1)
if len(sys.argv) < 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
num_words = get_num_words(sys.argv[1])
letter_count = get_letter_count(sys.argv[1])
sorted_letters = sorted1(sys.argv[1])

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for p in range(len(sorted_letters)):
          print(sorted_letters[p])
print("============= END ===============")