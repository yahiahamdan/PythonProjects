import sys 
print("welcome to the password generator")

def ViewMethod():
  with open('password.txt','r') as f:
      for line in f.readlines():
       data=line
       print(data.strip())
       #information =line.rsplit("|")
       #print(information)
       return
def add():
    name =input("account Name :")
    pwd= input("password :")
    with open('password.txt','a') as f :
     f.write(f"{name}|{pwd} ")                 

while(True):
   inp= input("you want to add or view  if you want to quit press q ")

   if inp.lower() =='q':
       quit()
   if inp.lower()=='view':
       ViewMethod()
    
   if inp.lower()=='add':
       add()
       print("added succesffuly ")