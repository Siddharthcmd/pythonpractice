"""
given a string : "ABCDEFGH"

Create a dict with keys as string letter and value as 1

for e.g. :

{
    'A': 1
}

"""
st="ABCDEFGH"
#x=st.split("")
x=[*st]
print(x)
dic={}
for i in st: dic[i]=1
print(dic)