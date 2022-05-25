"""
Two strings are anagrams of each other if letters of one string can be 
rearranged to form the other string.

Given a string, find the number of pairs of substrings of the string 
that are anagrams of each other.

s = mom

all anagram pair [m, m] [mo, mo]

abba = 4 [a, a][ab, ba], [b, b], [abb, bba]
abcd = 0

"""
def sherlockAndAnagrams(s):
    my_dict = {}
    for length in range(len(s)):
        for index in range(len(s) - length):
            key = ''.join(sorted(s[index:index+length+1]))
            if key in my_dict:
                my_dict[key] += 1
            else:
                my_dict[key] = 1
    count  = 0
    # my_dict = Counter(s)

    # for i in range(2, len(s)):
    #     sub_string = s[0:i]
    #     my_dict[''.join(sorted(sub_string))] += 1
        
    #     l = len(sub_string)
    #     for j in range(1, len(s)):
    #         if j+l <= len(s):
    #             sub_string_2 = s[j:j+l] 
    #             my_dict[''.join(sorted(sub_string_2))] += 1
    
    for k, v in my_dict.items():
        count += v*(v-1)//2
    
    return count
    
    

print(sherlockAndAnagrams("kkkk"))