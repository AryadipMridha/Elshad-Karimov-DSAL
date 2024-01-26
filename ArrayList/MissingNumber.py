#Taking user input list
lval=int(input("Enter last value:"))
ulist=[]
for i in range(lval-1):
    item=int(input(f"number {i}:"))
    ulist.append(item)

#Finding Missing nuumber
def findmissing(mylist,lastvalue):
    sum1=(lastvalue*(lastvalue+1))//2
    sum2=sum(mylist)
    print(f"{sum1-sum2} is missing")

#calling
findmissing(ulist,lval)

