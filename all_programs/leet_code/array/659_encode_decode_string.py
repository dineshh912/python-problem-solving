"""
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

"""

def encode(strs):
    res = ""
    for i in strs:
         res += str(len(i)) + "#" + i

    return res
   
def decode(strs):
    res, i = [], 0

    while i < len(strs):
        j = i
        while strs[j] != "#":
            j += 1
        
        length = int(strs[i:j])

        res.append(strs[j+1: j+1+length])
        i = j+1+length
    
    return res


#print(encode(["lint","code","love","you"]))

print(decode("4#lint4#code4#love3#you"))