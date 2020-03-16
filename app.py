import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        choice = input('Did you mean {} instead (y/n) : '.format(get_close_matches(word, data.keys())[0]))
        # choice = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if choice == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == 'n':
            return "The word doesn's exists."
        else:
            choice = input('Invaild request (y/n) : ')
    else:
        return "The word doesn't exists"

user_search = input('Search : ').lower()
output = translate(user_search)

if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)
# print((translate(user_search)))