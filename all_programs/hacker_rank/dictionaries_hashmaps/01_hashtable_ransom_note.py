"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

Example:

magazine = "attach at dawn"
note = "Attack at dawn"

ns = No

6 4
give me one grand today night
give one grand today

yes

two times three is not four
two times two is four

ans: no ( two appear only once in the magazine)

"""

def checkMagazine(magazine, note):
    pass


if __name__ == "__main__":
    mag = "ive got a lovely bunch of coconuts"
    note = "ive got some coconuts"
    print(checkMagazine(mag, note))