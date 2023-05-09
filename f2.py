"""
Given a list = [11, 22 ,33 ,44 ]
Create a dict with keys as the list elements and values as the square of the key
for e.g : 
{
    11: 121
}

"""

lis=[11,22,33,44]
def dick(l1):
    dic={}
    for i in lis: 
        dic[i]=i*i
    return dic
print(dick(lis))

