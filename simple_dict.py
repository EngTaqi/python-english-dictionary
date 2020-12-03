import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(word):
        if word in data:
            return data[word]
        elif len(get_close_matches(word,data.keys())) > 0:
            for i in range(len(get_close_matches(word,data.keys()))):
                 YN=input("Did you mean (%s) instead? Enter Y if Yes or N if No " % get_close_matches(word,data.keys())[i])
                 if YN.lower()=="y":
                    return data[get_close_matches(word,data.keys())[i]]
        elif YN.lower()=="n":
                     return "The word does not exist please check it"
        else:
            return "I dont understand what do you want"
        

word=input('enter a word ')
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
