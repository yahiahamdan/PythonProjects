print("lets play the game toaday")
playing=input("do you want to play\n")
score=0
if(playing.lower() != "yes"):
    quit()
print("okay lets play")
answer=input("what does cpu stand for?")
if answer=="centeral processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("what does gpu stand for?")
if answer=="ay 7aga":
    print("correct")
    score+=1
else:
    print("incorrect")

answer=input("what does  stand for?")
if answer=="no":
    print("correct")
    score+=1
else:
    print("incorrect")

print(f"your score is  : {score}") 
quit()