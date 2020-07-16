# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 08:18:45 2019

@author: Alok Ranjan
Topic: While and for loop
"""
#==============================================================================
# While loop - is used to execute set of instruction while
# condition is true.
# syntax
# while(condition);
#     python statement
# else:
#     python statement
# 
#==============================================================================
x=int(input("Enter x"))
count=0
while(x<=50):
    x=x+5
    count+=1
print("Count is ", count)

#Create a function to find how many weeks it will take
#to accumulate 5000 when i save amt x per week.
#x will be given by user

def find_weekcount(x):
    count=0
    amt=0
    while(amt<5000):
        amt=amt+x
        count=count+1
    return(count);

find_weekcount(5000)


# if i am depositing my money in bank, and bank gives 
# 8% interest per year. find how many year it will take
# to get 500000 if i am depositing 20000/- per year.


def find_yearcount(peryear,reqamt,roi):
    count=0
    amt=0
    #if (reqamt<peryear): return (count)
    while(amt<reqamt):
        amt=amt+peryear
        amt=amt+amt*roi/100
        count=count+1
    return(count);

find_yearcount(20000,500000,8)

#when and how to use else
time=10
while(time<12):
    print("Time:"+str(time)+" AM Good Morning")
    time+=1
else:
    print("Good Afternoon")
print("Have a good day")

#==============================================================================
# for loop - is used to execute set of intructions for:
#     each item in collection
# syntax
#     for item in collection:
#         python statements
#         
#==============================================================================

for i in [10,20,30]:
    print(i)


#write python code to increment all values in list by 
#10. create list as follows [1,11,21,31,41]

newlist=[]
mylist=[1,11,21,31,41]
for i in mylist:
    i+=10
    print(i)
    newlist.append(i)

print(newlist)

#create a function to find yearly balance if i am 
#depositing 1000/- per month for 5 year in bank.
#and bank is giving interest 4% per annum.
#assume interest is compounded monthly

def final_amt(permonth,year,roi):
    amt=0
    peryearamt=[]
    for y in range(1,year+1):
        for m in range(1,13):
            amt=amt+permonth
            amt=amt+amt*float(roi)/1200
        peryearamt.append(round(amt))
    return(peryearamt);

print(final_amt(1000,5,4))

#==============================================================================
# #loop control statements
# #break - will stop loop
# #continue - will stop current iteration and continue for next
# #pass - will pass execution to next statement, it do nothing
# 
#==============================================================================
for i in "python":
    print(i)
    

for i in "python":
    if (i=="t"): break
    print(i)
    
for i in "python":
    if (i=="t"): continue
    print(i)
        

for i in "python":
    if (i=="t"): pass
    print(i)    



















