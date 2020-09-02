# import datetime

# x = datetime.datetime.now()

# print(x.strftime("%d") + "/" + x.strftime("%A") + "/" + x.strftime("%B") + "/" + x.strftime("%Y"))

# print(x.strftime("%X") + " " + x.strftime("%p"))

# print(x.strftime("%c"))

# realDateTime = datetime.datetime.now()
# print(realDateTime.strftime("%c"))

# for i in "Datacamp":
#     if i == 'a':
#         print (i)

# print("-----------------")

# for i in range(10):
#     for j in range(i):
#         print (i, end=' ')
#     print()




# Python program to concatenate 
# the result of two range functions 
from itertools import chain 
   
# Using chain method 
print("Concatenating the result") 
res = chain(range(5), range(10, 20, 2)) 
  
for i in res: 
    print(i, end=" ") 