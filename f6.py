"""
given a list of lists
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

print the transpose of the matrix

"""
l1=[[1,5,6],
    [2,3,9],
    [2,3,4]]

print(l1)
c=0
l=[]
while c<len(l1):
    print("sid")
    l.append([i[c] for i in l1])
    c+=1
print(l)