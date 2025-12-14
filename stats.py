def get_book_text(filepath): 
        with open(f"{filepath}") as f: 
                file_contents = f.read()
        return file_contents
def get_num_words(text):
        word_list = text.split()
        num_words = len(word_list)
        return num_words 
def get_num_letters(text):
        letter_list = (",",".","?","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","@","#","$","%"," ","^","&","*","-","=","+")
        lower_case_text = text.lower()
        dictionary_count = {}
        for letter in letter_list:
                temp_letter_count = lower_case_text.count(letter)
                dictionary_count[letter] = temp_letter_count
        return dictionary_count

