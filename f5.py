"""
given a list of lists
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

print the diagonal values

1,5,9

"""
l1=[[1,5,6],
    [2,3,9],
    [2,3,4]]
c=0
l=[]
for i in l1:
    l.append(i[c])
    c+=1
print(l)
    