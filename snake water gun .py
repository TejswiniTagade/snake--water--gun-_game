user_count=0
system_count=0
import random
# for user winner count
def user_winner():
    global user_count
    print("user is winner")
    if user == "true":
        pass      
    user_count+=1
    print("count of use: ",user_count)
# for system winner count
def system_winner():
    print("system is winner")
    global system_count
    if op == "true":
        pass
    system_count+=1
    print("count of system: ",system_count)
i=0
while(i<10):
    # system will generate option
    options=["snake","water","gun"]
    op=random.choice(options)
    # user will select option
    user=input("enter your option snake or water or gun: ")
    #check input 
    if op=="snake" and user=="water":
        system_winner()
    elif op=="water" and user=="snake": 
        user_winner()
    elif op=="gun" and user=="snake":
        system_winner()
    elif op=="snake" and user=="gun":
        user_winner()
    elif op=="gun" and user=="water":
        user_winner()
    else :
        system_winner()
    i+=1
# for winner
if user_count>system_count:
    print("congratulation user you win")
else:
    print("try it again ")
    
