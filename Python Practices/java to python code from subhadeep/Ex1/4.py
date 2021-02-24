days = int(input())
totalFine = 0
count  = 1
while days!=count:
    if count<=5:
        totalFine+=40
    elif count>5 and count<=10:
        totalFine+=65
    elif count>10:
        totalFine+=80
    count+=1
print(totalFine, "paisa")
