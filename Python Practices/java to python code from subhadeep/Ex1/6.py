num = int(input())
truediv = str(num//7)
if(num%7==0 and int(truediv[len(truediv)-1])==7):
    print("buzz")
else:
    print(False)
