from stats import get_book_text
from stats import get_num_letters  
def main():
	text = get_book_text("books/frankenstein.txt")
	dic_out_put = get_num_letters(text)
	print(dic_out_put)
	

main()

