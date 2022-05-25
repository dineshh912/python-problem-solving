"""
Harold is a kidnapper who wrote a ransom note, 
but now he is worried it will be traced back to him through his handwriting.
He found a magazine and wants to know if he can cut out whole words from it and use 
them to create an untraceable replica of his ransom note. 
The words in his note are case-sensitive and he must use only whole words available in the magazine. 
He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, 
print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

Example:

magazine = "attack at dawn" note ="Attack at dawn

case is not matching so answer is No

6 4
give me one grand today night
give one grand today

yes

6 5
two times three is not four
two times two is four

No

"""
from collections import Counter

def checkMagazine(magazine, note):
    
    magazine_list = magazine.split(" ")
    note_list = note.split(" ")

    magazine_dict = Counter(magazine_list)
    note_dict = Counter(note_list)

    for key, value in note_dict.items():
        if key in magazine_dict and magazine_dict[key] >= value:
            continue
        else:
            return "No"

    return "Yes"
    



print(checkMagazine("two times three is not four", "two times two is four"))

