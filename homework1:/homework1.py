#File homework1 py
#--- Vairbales and Data Types---
a = 10
print(a)
print(type(a))
b = 1.5 
print(b)
print(type(b))
c=3j
print(c)
print(type(c))
d="hello"
print(d)
print(type(d))
e = [1, 2, 3]
print(e)
print(type(e))
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
g = (1,2)
print(g)
print(type(g))
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
i = True
print(i)
print(type(i))
j = None
print(j)
print(type(j))
k = [True, "blue", 12]
print(k)
print(type(k))
l = str(14)
print(l)
print(type(l))
m = 1e4
print(m)
print(type(m))
""""""
#I was able to find around 9 different data types
#Strand, Boolean, List, integer, float, tuple, nonetype, complex, and dict
#a was the only int, b, and m were both floats, c was the only complex, d and l were the only strands e k, were both lists, i was the only boolean, and j was the only nonetype
# The data type of l was strand, this was because we used the command str to turn an integer into strand.
#  another data types would be set which is like {1, 2, 3}
n = {1, 2, 3}
print(n)
print(type(n))
""""""
#--- Booleans ---
print(10>9) #True
print(10 == 9) #False
print(10 <= 9) #False
print(bool("abc"))#True
print(bool(123))#True
print(bool(["apple", "cherry", "banana"]))#True
print(bool(True))#True
print(bool(False))#False
print(bool(0))#False
print(bool(""))#False
print(bool(()))#False
print(bool([]))#False
print(bool({}))#False
print(bool(True and False))#False
print(bool(True and True))#True
print(bool(False and False))#False
print(bool(True or False))#True
print(bool(True or True))#True
print(bool(False or False))#False
print(bool(not(False)))#True
print(bool(not(True)))#False
""""""
#I noticed that when returning True or False, it depended on either the sign or the words it had like (True) gave true and (false) gave false
#The ones that had nothing in them like[] or {} were false, idk why
#An expression would be like: Print(bool(11+6 == 17)) because 11 plus 6 is 17
#One that would be false is just print(bool(6 == 7)) which it doens't
""""""
#----Operators---
print(10 + 5) #addition
print(10 - 5) #subtraction
print(2 * 4)#multiplication
print (6 / 3) #division
print(5 % 2) #remainder
print(3 ** 2)#exponentials
print( 15 // 2)#dividision with rounding down
print(5 == 2) #Gives back false, since 5 isn't equal to 2
print(10 != 10)#gvies back false, 10 IS equal to ten
print(2<5) #gives back true, 5 is greater than 2
print(12>5)#gives back true, 12 is greater than 5
print(5<=6)#gives back true 6 is greater than or equal to 5
print(1>=10)#gives back false, 1 is not greater than or equal to 10
x = 5 
print(x)#spits out 5
x += 5#adds 5 to 5 giving 10
print(x)
x -=4#subtracts 4 from 10 giving 6
print(x)
x *= 3#multiplies 3 to 6 giving 18
print(x)
""""""
 #an operator of and, makes sure both things are true, to spit out true, and if even one is false its then false. It checks two condiitons for example: print(bool( 5==5 and 5!=8))
 #Then or, makes sure either one or the other of a condiiton is true, so basically: Print(bool(6 == 7 or 6<= 7))
 #The operator not, then just flips the true or false aspect of the boolean, making the opposite true. So print(bool(not(5=8)) then print(bool(not(5==5))
# / is dividison while // is diviion to the nearst whole number, since / gives a float
# gives you the divion remainder of two numbers, while / just gives you a float
#you would use %, print(10 % 7), giving me the whooe number of remainder from 10 / 7
#assignments operators take a varibles and to an operation to the variable itself, changin its instrinsic property.

""""""
#---3.5 Terminal Commands
#Cd
#Changes direcotires, use it to move from one folder to another
#Example: cd Python_Decal_Fall2025/Michael

#ls, using ls to show all folders thats on your laptop, showing all parent folders.
#example: ls when in Python_Decal_Fall2025

#ls -a, shows kidden folders that are in your computer, that you might not see originally
#ls -a, to check for folders that you might not now are there

#mkdir, it to create a folder autmoatically inside a parent folder, allowing you to make a program automatically
# example: mkdir homework2.py to automatically make another fiel for homework

#cat, can display a file contents, and shows everything inside of the file
#cat homework2.py.

#pwd shows the direcotry of where exaclty you are and what's inside of the things you're looking at.
#example: pwd to figure out what folder you need to get to

#cd ..is to go up one directory of a parent folder
#cd to go from michael back to Pyhton_Decal_Fall2025

#cd . to stay in current directory
#cd . idk why someone would use this

#cd ~ going to your home directory
#cd ~ takes me all the way back to users/michaeljoliver

#cp is to copy files, and then you may rename is
#cp homework2.py backuphomework.py

#mv to move a file to somewhere else
#example: mv homework2.py users/michaeljoliver

#rm is to delete a file
#rm backuphomework.py

#clear to clear the terminal
#example clear, when theres too many errors and texts to clear it

#grep, this allows to search things inside your files
#grep "print" to see the lines that contain the word "python"

""""""
#Questions for 3.5
#date, shows you the current hours, minutes, and sexconds and the time you're on
#date: Sat Sep, 10:42:17 PDF 2025

#echo, this prints texts to the terminal just to see them
#exmaple: echo "Apples" : Apples

#whoami, which shows your current username
#whoami: Michaeljoliver

#ls and ls -a, one reads your files, while the other allows you to see hidden files which aren't normally shown.
#A hidden file starts with a dot, and they avoid clutter
#3 other flags would be: ls -l, which shoes a long list of details, ls -R, shoes files in subfolders throughouly, and then ls -t, which sorts by the time you last used them

""""""
#---Running your script----
