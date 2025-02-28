from stats import get_book_text, get_character_count, sort_character
import sys

def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = len(text.split())
    print(f"Found {word_count} total words")
    character_count = get_character_count(text)
    print("--------- Character Count -------")
    sorted_list = sort_character(character_count)
    for char_dict in sorted_list:
        char = list(char_dict.keys())[0]
        if char.isalpha():
            count = char_dict[char]
            print (f"{char}: {count}")
    print("============= END ===============")        
        
        
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
print ("============ BOOKBOT ============")
print (f"Analyzing book found at {sys.argv[1]}")
print ("----------- Word Count ----------")
main()