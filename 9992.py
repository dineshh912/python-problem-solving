"""
 *  This problem was recently asked by google
 *  
 *  Given a list of numbers and a number k, return whether any two numbers from the list 
 *  add upto k
 * 
 *  for example, given [10, 15, 3, 7] and k of 17, return true since 10+7 is 17
 * 
 * Bonus: can you do this in one pass?
 */
"""
from calendar import c


lstNumbers = [10, 15, 3, 7]

k = 17

def checkNumber(lstNumbers, k):
    for i in range(len(lstNumbers)):
        for j in range(len(lstNumbers)):
            if i!=j and (lstNumbers[i] + lstNumbers[j]) == k:
                return True
    
    return False




def checkNumberSingle(lstNumbers, k):
    checked = set()
    for i in lstNumbers:
        if k - i in checked:
            return True
        checked.add(i)
    return False

# print(checkNumber(lstNumbers, k))

print(checkNumberSingle(lstNumbers, k))