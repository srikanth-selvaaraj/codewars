cc = "skippy"
string_list = list(cc)
if len(cc) > 4:
    i = 0
    while i <= len(cc)-5:
        string_list[i] = '#'
        i +=1
    print("".join(string_list))
elif len(cc)<4 and len(cc)>0:
    print(cc)
else:
    