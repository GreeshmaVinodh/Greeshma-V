def count(L):
    result={}
    for j in range(1,10):
        count=0
        for i in L:
            if i%j == 0:
                count+=1
        result[j]=count
    return(result)



L=[1,2,8,9,12,46,76,82,15,20,30]
print(count(L))

# Output
# {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}