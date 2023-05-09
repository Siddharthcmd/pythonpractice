"""
given a list of lists
    [
        [1,2],
        [3,4]
    ]

print the first column 
1,3
"""
l1=[[1,5,6],
    [2,3,9],
    [2,3,4]]
def first_row(l1): return [i[0] for i in l1]
print(first_row(l1))