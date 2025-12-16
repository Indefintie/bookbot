from stats import get_book_text
from stats import get_num_letters 
from stats import get_num_words
from stats import order_dic 
import sys
def main():
	if len(sys.argv) == 2:
		text = get_book_text(f"{sys.argv[1]}")
		dic_out_put = get_num_letters(text)
		num_of_words = get_num_words(text)
		ordered_dicshon = order_dic(dic_out_put)
		
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {sys.argv[1]}...")
		print("----------- Word Count ----------")
		print(f"Found {num_of_words} total words")
		print("--------- Character Count -------")
		for item in ordered_dicshon:
			if item["char"].isalpha():
				print(f"{item['char']}: {item['num']}")
		print("============= END ===============")
	else:
		print("Usage: python3 main.py <path_to_book>")
		return sys.exit(1)
	

main()

