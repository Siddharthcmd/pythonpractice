s="abcdefzghibxjkclmnodapqbrstuvwxyz"
n = len(s)
max_len = 0
start = 0
char_map = {}
lar_string=set()
for i in range(n):
    if s[i] in char_map and start <= char_map[s[i]]:
        start = char_map[s[i]] + 1
    else:
        max_len = max(max_len, i - start + 1)
        lar_string.add(s[start:start+max_len])
    char_map[s[i]] = i


print(max_len) 
print(max(lar_string))