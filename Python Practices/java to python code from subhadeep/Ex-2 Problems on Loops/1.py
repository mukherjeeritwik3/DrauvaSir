# Program to find prime number series from upper limit to lower limit

lower = int(input("Enter the lowerlimit: "))
upper = int(input("Enter the upperlimit: "))

for i in range(lower,upper+1):
    if i >1:
        for j in range(2,i):
            if i%j==0:
                break

        else:
            print(i)