"""
Given two strings, determine if they share a common sub string.
Sub string may be a small as one character

s1 = "and"
s2 = "art"

common sub string a

"""

def twoStrings(s1, s2):
    # this is bruntforce method
    flag = False
    for i in list(s1):
        if i not in list(s2):
            continue
        else:
            flag = True
            break
    
    if flag:
        print("YES")
    else:
        print("NO")


def twoStrings_2(s1, s2):
    # Write your code here
    print(set(s1))
    print(set(s2))
    print(set(s1) & set(s2))
   # return 'YES' if set(s1) & set(s2) else 'NO'

twoStrings_2("and", "art")