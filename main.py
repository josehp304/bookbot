import sys
from stats import count_words, char_dict
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        print(file_contents)


def main(path):
    num_words=count_words(path)
    print("Found "+ str(num_words) + " total words")
    char_dict_result = char_dict(path)
    for key in char_dict_result:
        print(key+": "+str(char_dict_result[key]))
    sys.exit(0)

args = sys.argv
if (len(args) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(args[1])