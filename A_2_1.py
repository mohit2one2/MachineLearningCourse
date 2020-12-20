i,j = 1,1
for i in range(5):
    for j in range(i) :
        print("*",end = " ")
    print()
print("* * * * *")
i = 4
while i>0:
    for j in range(i):
        print("*",end = " ")
    print()
    i = i - 1

