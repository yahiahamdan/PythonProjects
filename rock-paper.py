from math import radians
import random
freq={1:2,2:4,3:5}
userWins=0
computerWins=0
options=['rock','paper','scissor']
maxKey=max(freq)
print(f" no is freq {maxKey}:{freq[maxKey]} ")
print("please enter a  rock/paper/scissor  or q to quit")
random_number=random.randint(0,2)
while(True):
 inp=input()
 if(inp.lower()=='q'):
    if(userWins>computerWins):
        print(f"congraluation you won with a score {userWins} / {computerWins}")
    elif(computerWins>userWins):
        print(f"losttt with score {computerWins} /{userWins}")
    else:
        print("you have same results you can try again") 
    quit()

 if(inp not in options):
     print('please enter a valid ')
 computerPicks=options[random_number]
 if inp=="rock" and computerPicks=="scissor":
     print("you won")
     userWins+=1
 elif inp=="paper" and computerPicks=="rock":
  print("you won")
  userWins+=1
 elif inp=="scissor" and computerPicks=="paper":
     print("you won")
 else :
     print("computer wins")
     computerWins+=1

#rock 0 paper :1  scissors:2  
