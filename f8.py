"""
Given a string 

s1 = "ABCDEFFGGAAA"

print the first repeating letter

here its b
"""



def first(s):
    dic={}
    for i in s:
        if dic.get(i) is not None:
            return i
        dic[i]=1
        

def get_first_non_repeating_character(input_string):
    ch_count_map={}
    for index, ch in enumerate(input_string):
        if ch_count_map.get(ch) is None:
            ch_count_map[ch]={'count':1,'index':index}
            continue
        ch_count_map[ch]['count']+=1
    for ch in (ch_count_map):
        if int(ch_count_map[ch]['count'])==1:
            return ch_count_map[ch]['index']


s1 = "IBXCDEFFGGAAAAKSDHJFJOIAEH"
print(get_first_non_repeating_character(s1))