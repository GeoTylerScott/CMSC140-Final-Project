from pathlib import Path
from PIL import Image #package to open image with a terminal command

def Archean(): #creates a function that opens up a text file in read mode 
    with open("Archeon.txt") as f:
        for line in f.readlines():
            print(line)
def CoE(): #creates a function that opens up a text file in read mode
    with open("Creation_Of_Earth.txt") as f: 
        for line in f.readlines():
            print(line)
def Paleoproterozoic (): #creates a function that opens up a text file in read mode
    with open("Early_Portoerozoic.txt") as f:
        for line in f.readlines():
            print(line)
def Hadean():#creates a function that opens up a text file in read mode
    with open("Hadean.txt") as f:
        for line in f.readlines():
            print(line)
print("Hello! \n welcome to the History of Earth during its early age\n take a look at some options, press the specific letter to the given eon or type out your answer\n can you find the secret?")
print("\n Here are some options \n C= Creation of Earth (~4.6 Billion Years) \n H= Hadean(~4.0 Billion Years) \n A= Archeon(~2.5 Billion Years) \n P= Paleoproterozoic (~1.5 Billion Years \n If you want to quit press x \n")   
inputs = [] #creates empty list
HoldList=["e", "h", "c", "a"] #a list of varibles that is stored 
HoldList.sort() #sorts the list into alphabetical order 
User=input("Enter your choice, ") #input the user can put

while User.lower() != "x": #creates a loop to iterate over each if statement, once x is pressed the loop breaks
    
    if User.lower() == "a" or User.lower() == "archeon" : #makes the input of the user to lower case and if a user inputs leter a or types Archeon run through if statement 
            Archean()
            PicArcheon=input(" Would you like to see a artist depiction of the Archeon? Type Yes(y) or no(n) , ") #calls the function
            if PicArcheon.lower() == "yes" or PicArcheon.lower() =="y": #nesting, after the function is called a prompt asks another input if the user wants to open a image or not
                im = Image.open(r"Archeon.jpeg") 
                im.show()#shows the image
            else:
                print("Ok moving on")
            inputs.append(User.lower()) #adds what the input to the empty list
    elif User.lower() == "c" or User.lower() == "creation of earth" :
            CoE()
            PicCoE=input("Would you like to see a artist depiction of the early earth before it became a planet? Yes(y) or no(n), ")
            if PicCoE.lower() == "yes" or PicCoE.lower() == "y":
                im = Image.open(r"Creatioin_Of_Earth.jpeg")
                im.show() 
            else:
                print("Ok moving on")
            inputs.append(User.lower()) #similar to archeon just calls a different function is called 
    elif User.lower() == "h" or User.lower() == "hadean":
            Hadean()
            PicHadean = input("Would you like to see a artist depiction of the Hadean? Type Yes(y) or no, ")
            if PicHadean.lower()== "yes" or PicHadean.lower()== "y":
                im = Image.open(r"Hadean.jpeg")
                im.show()
            else:
                print("Ok moving on") 
            inputs.append(User.lower())
    elif User.lower() == "p" or User.lower() == "paleoproterozoic" : #similar to archeon just calls a different function is called 
            Paleoproterozoic ()
            PicEPort=input("Would you like to see a artist depiction of the Paleoproterozoic? Type Yes(y) or no(n), ")
            if PicEPort.lower() =="yes":
                im = Image.open(r"Paleoproterozoic.jpeg")
                im.show()
            else:
                print("Ok moving on")
            inputs.append(User.lower())
    else:
            print("try again") #if user inputs anything that is not on option or x
            
    print("\n Would you like to enter another era? \n C= Creation of Solar System (~4.6 Billion Years) \n H= Hadean(~4.0 Billion Years) \n A= Archeon(~2.5 Billion Years) \n P=Paleoproterozoic (~1.5 Billion Years \n Press x to quit")


    User = input("Enter your choice, ")
    
inputs.sort() #sorts the inputs that were put into the empty list from the user
HoldList.sort()

inputs_sets=set(inputs) #creates a new varabiole that stores the empty list into a set.
HoldList_sets=set(HoldList) #holds the list created from HoldList varible into a set

if HoldList_sets==inputs_sets: #when the Hold sets is equal to the input set than runs the print statement and image opener
    print(" congrats you found the secret, enjoy the geology scale. Thanks for playing!")
    im = Image.open(r"GeoTimeScale.jpeg")
    im.show()
else:
    print("thank you for playing") #If someone doesnt add all the inputs correctly or  (ends early)






# Sources 
# https://www.sciencephoto.com/media/168619/view/archaean-earth
# https://www.sciencephoto.com/media/168619/view/archaean-earth
# https://www.britannica.com/science/Hadean-Eon
# https://www.britannica.com/science/Archean-Eon
# https://ucmp.berkeley.edu/precambrian/archean_hadean.php
# https://www.geologypage.com/2013/10/archean-eon.html
# https://geo.libretexts.org/Bookshelves/Geology/Book%3A_An_Introduction_to_Geology_(Johnson_Affolter_Inkenbrandt_and_Mosher)/08%3A_Earth_History/8.04%3A_Archean_Eon
# https://www.geeksforgeeks.org/python-pil-image-open-method/
# https://www.geologypage.com/2014/01/paleoproterozoic-era.html
# https://www.corzakinteractive.com/earth-life-history/31_proterozoic.htm