mylist=[20,50,60,70,90]
print(mylist)
if len(mylist)>1:
    mylist[0],mylist[-1]=mylist[-1],mylist[0]
print(mylist)    
