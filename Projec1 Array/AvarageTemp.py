DayCount=int(input("How many days you want to find average of ?"))
temps=[]
summation=0
for i in range (1, DayCount+1):
    record=int(input(f"Day {i}'s high temp :"))
    temps.append(record)


# avarage
for i in range(len(temps)):
    summation+=temps[i]
average = summation//DayCount


#which days are over average
for i in range(len(temps)):
    if (temps[i]>average):
        print(f"Day {i+1} is above average temperature")
       

