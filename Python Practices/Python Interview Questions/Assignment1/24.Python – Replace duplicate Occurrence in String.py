"""Sometimes, while working with Python strings, we can have problem in which we need to perform the replace of a
word. This is quite common task and has been discussed many times. But sometimes, the requirement is to replace
occurrence of only duplicate, i.e from second occurrence. This has applications in many domains. Let’s discuss
certain ways in which this task can be performed.


"""

st = "Gfg is best . Gfg also has Classes now. Classes help understand better . "
st_arr = st.split(' ')
replace_arr = ['It','They']
count = 0
for i in range(len(st_arr)):

    if(st_arr[i]=='Gfg'):
        count += 1
        if(count>1):
            st_arr[i] = replace_arr[0]

ct = 0
for i in range(len(st_arr)):

    if(st_arr[i]=='Classes'):
        ct += 1
        if(ct>1):
            st_arr[i] = replace_arr[1]

print(' '.join(st_arr))