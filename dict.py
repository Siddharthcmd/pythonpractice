def dict1(d):
    pass

dic1 = { 1 : "hello", 2 : "world" , "key": 100, 100: "value"} 
"""
iterate over the dict to print the below format 
1==>hello
2==>world

print only dict values as a list
print only dict keys as a list

"""
print(dic1[1])
for key in dic1:
    print(key,"==>",dic1[key])
print(list(dic1.keys()))
print(list(dic1.values()))

"""
modify the dict,
change the value if the key is a even number , to "even"

then print the dict 

1==>hello
2==>even

"""
for key in dic1:
    if str(key).isnumeric() and key%2==0:
        dic1[key]="even"

print(dic1)

"""
update the dict to add 
d1 = {
    200: "value1",
    300: "value2"
}

"""
d1 = {
    200: "value1",
    300: "value2"
}
dic1.update(d1)

"""
some_keys = [100, 200, 300, 400, 500]

check the dict for all the keys present in the above list 
and display the value if present otherwise print None

"""
some_keys = [100, 200, 300, 400, 500]
for key in some_keys:
    if dic1.get(key)!=None:
        print(key,":present and value is:",dic1[key])
    else:
        print("none")
