"""
str_list = ['radar', 'rotor', 'malayalam', 'hello', 'world']

iterate through the list and output the total number of palindromes 

expected output : 3

"""
def count_palindrom(l):
    count=0
    for i in l:
        if i==i[::-1]:
            count+=1
    return count

str_list = ['radar', 'rotor', 'malayalam', 'hello', 'world']
print(count_palindrom(str_list))