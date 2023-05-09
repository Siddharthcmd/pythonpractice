s="AbCcBad"
ans_str=""
rep_s=""
start=0 
for c in s:
    if len(ans_str)==0 or ans_str[-1].lower()!=c.lower():
        ans_str=ans_str+c
    else:
        ans_str=ans_str.replace(ans_str[-1],"")
print(ans_str)
        