def series(a):
    x=[]
    for i in range(1,a+1):
        if(i%2!=0):
            x.append(i)
    print(x)
a=int(input("Enter the value of a: "))
series(a)

# Sample output 1
# Enter the value of a: 5
# [1, 3, 5]
# Sample output 2
# Enter the value of a: 6
# [1, 3, 5]
# Sample output 3
# Enter the value of a: 3
# [1, 3]
# Sample output 4
# Enter the value of a: 4
# [1, 3]