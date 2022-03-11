"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. 
Answers within 10-5 of the actual answer will be accepted.

"""

def averge_sal(list_of_sal):
    min_sal = min(list_of_sal)
    max_sal = max(list_of_sal)

    list_of_sal.remove(min_sal)
    list_of_sal.remove(max_sal)

    return sum(list_of_sal) / len(list_of_sal)


sal = [100, 40000, 200, 500, 600, 50]

averge_sal(sal)