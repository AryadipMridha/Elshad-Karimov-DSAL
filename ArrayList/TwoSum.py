def twosum(mylist,num):
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            if mylist[i]==mylist[j]:
                continue
            elif mylist[i]+mylist[j]==num:
                print([i,j])
twosum([2,3,5,4],6)
