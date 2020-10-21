# put your code here.
import sys
def word_count():
    file_name = sys.argv[1]
    file_path = open(file_name)
    list_of_words = {}
    # new_list = []
    replace_words = [',' ,'?' ,'.']
    for line in file_path:
        words = line.split()
        for word in words:
            if word.isalpha():
                word = word.lower()            
                list_of_words[word] = list_of_words.get(word,0) + 1 
            else:
                for punct in replace_words:
                    word = word.replace(punct, "")
                word = word.lower()            
                list_of_words[word] = list_of_words.get(word,0) + 1 
    return list_of_words

                 

  


print(word_count())


