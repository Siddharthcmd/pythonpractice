"""

panlin_str = 'radarrotormalayalam'

print all the palindromes present in the above string

expected output : ['radar', 'rotor', 'malayalam']

"""
panlin_str = 'radarrotormalayalam'
def find_palin(s):
    s=[]
    for i in range(len(panlin_str)):
        for j in range(i,len(panlin_str)):
            s1=panlin_str[i:j+1]
            if len(s1)>=3 and s1==s1[::-1]:
                s.append(s1)
    return s
print(find_palin(panlin_str))  
        
        
