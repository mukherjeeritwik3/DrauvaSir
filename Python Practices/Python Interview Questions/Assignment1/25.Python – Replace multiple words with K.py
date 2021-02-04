"""Sometimes, while working with Python strings, we can have a problem in which we need to perform a replace of
multiple words with a single word. This can have application in many domains including day-day programming and school
programming. Lets discuss certain ways in which this task can be performed. """

test_str = 'Geeksforgeeks is best for geeks and CS'

#List to change the words

word_list = ['best','geeks','for']
replace_word = 'gfg'
test_arr = test_str.split(' ')
print(test_arr)
for i in range(len(test_arr)):
    for j in range(len(word_list)):
        if test_arr[i] == word_list[j]:
            test_arr[i]=replace_word
print(' '.join(test_arr))