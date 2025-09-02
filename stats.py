def count_words(path):
    with open(path) as f:
        file_contents = f.read()    
        return len(file_contents.split())
def char_dict(path):
    with open(path) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        dictt={}
        for char in file_contents:
            if(char !=" "):
                if char in dictt :
                    dictt[char] += 1
                else:
                    dictt[char] = 1
        sorted_dict=dict(sorted(dictt.items(),key=lambda x:x[1],reverse=True))
    return sorted_dict

