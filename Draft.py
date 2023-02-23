from pathlib import Path
def Archeon():
    with open("/Users/tylerscott/Downloads/Python_2023/Final_Project/Archeon.txt") as f:
        for line in f.readlines():
            print(line)
#Archeon()
def CoE():
    with open("/Users/tylerscott/Downloads/Python_2023/Final_Project/Creation_Of_Earth.txt") as f:
        for line in f.readlines():
            print(line)
def EPortoerozoic():
    with open("/Users/tylerscott/Downloads/Python_2023/Final_Project/Early_Portoerozoic.txt") as f:
        for line in f.readlines():
            print(line)
def Hadean():
    with open("/Users/tylerscott/Downloads/Python_2023/Final_Project/Hadean.txt") as f:
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
    print("try again")

# I still need to add the information into the text files. I am also going to add a while loop once everything
# is done. Within the if else statment I am going to add more choices rather to see a graph if applicable 
# or add more terminal interactions within each statement . 
