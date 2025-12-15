def get_book_text(filepath): 
        with open(f"{filepath}") as f: 
                file_contents = f.read()
        return file_contents
def get_num_words(text):
        word_list = text.split()
        num_words = len(word_list)
        return num_words 
def get_num_letters(text):
        low_text =text.lower()
        chars = list(low_text)
        char_list = {}
        for letter in chars:
                if letter in char_list:
                        char_list[letter] += 1
                else :
                        char_list[letter] = 1
        return char_list

def order_dic(dic_out_put):
        list_dic=[]
        for char, count in dic_out_put.items():
                tmp_merg = {"char": char, "num": count}
                list_dic.append(tmp_merg)
        def sort_on(items):
                return items["num"]
        list_dic.sort(reverse=True, key=sort_on)
       
        return list_dic






