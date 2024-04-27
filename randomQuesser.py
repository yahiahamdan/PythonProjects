import random 
"""
built in module in python 
"""

r=random.randrange(-5,11)
quesserNo=0
print("guess no between -5 and 11 \n")
while(quesserNo <15):
 try:
  inp=int(input())
 except ValueError:
     print("please enter a valid integer")
     continue 
   

 if(inp==r):
    print( f"cangrluation pro you have reached this limit with no of attempts {quesserNo}")
    quit()
 elif(inp < r):
    print("you number is less than number try again please \n")
    quesserNo+=1

 else :
   print("your number is greater than the number please get the less one \n ")
   quesserNo+=1