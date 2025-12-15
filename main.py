from stats import get_book_text
from stats import get_num_letters 
from stats import get_num_words
from stats import order_dic 
def main():
	text = get_book_text("books/frankenstein.txt")
	dic_out_put = get_num_letters(text)
	num_of_words = get_num_words(text)
	ordered_dicshon = order_dic(dic_out_put)
	
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {num_of_words} total words")
	print("--------- Character Count -------")
	for item in ordered_dicshon:
		if item["char"].isalpha():
			print(f"{item['char']}:{item['num']}")
	print("============= END ===============")
	
	

main()

