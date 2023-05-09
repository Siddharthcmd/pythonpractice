l1=[[1,5,6],
    [2,3,9],
    [2,3,4]]


def first_col(lis):
    l1=[]
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            if j==0:
                l1.append(lis[i][j])
    return l1
                
def diagonal(lis):
    l1=[]
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            if i==j:
                l1.append(lis[i][j])
    return l1

def transpose(lis):
    row=[]
    for i in range(len(lis)):
        col = []
        for j in range(len(lis[i])):
            col.append(lis[j][i])   
        row.append()
    return l1
    

print("first col:",first_col(l1))
print("diagonal:",diagonal(l1))
print("transpose:",transpose(l1))