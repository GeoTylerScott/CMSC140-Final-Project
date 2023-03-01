from pathlib import Path
def Archeon():
    with open("Archeon.txt") as f:#I can't get these to open because the path is absolute here, i would maybe make it a relative path? just have it open Archeon.txt rather than the whole path because they should be in the same folder
        for line in f.readlines():
            print(line)
#Archeon()
def CoE():
    with open("Creation_Of_Earth.txt") as f:
        for line in f.readlines():
            print(line)
def EPortoerozoic():
    with open("Early_Portoerozoic.txt") as f:
        for line in f.readlines():
            print(line)
def Hadean():
    with open("Hadean.txt") as f:
        for line in f.readlines():
            print(line)
print("Here are some options \n Creation of Earth (~4.6 Billion Years) \n Hadean(~4.0 Billion Years) \n Archeon(~2.5 Billion Years) \n Early Portoerozoic(~1.5 Billion Years")
User=input()

if User.lower() == "archeon":
    Archeon()
elif User.lower() == "creation of earth" :
    CoE()
elif User.lower() == "hadean":
    Hadean()
elif User.lower() == "early portoerozoic" :
    EPortoerozoic()
else:
    print("try again")   #prob should run back to the start again and actually let me try again

# I still need to add the information into the text files. I am also going to add a while loop once everything
    "I think a while loop would be good so that I could get info for another thing after it finishes rather than the program just ending"
# is done. Within the if else statment I am going to add more choices rather to see a graph if applicable 
    "a graph would be cool if you can do it"
# or add more terminal interactions within each statement . 
