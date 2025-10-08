

def say_goodbye(name):#defines my name
	print ("Goodbye", name) 
      #prints goodbye and them my name :3
name = "Michael"
print(f"Goodbye", name)
def Circle(radius): #Calculates the area of a circle given a radius A=PI*r**2
	Pi = 3.14 #defines PI as a float  
	Area = Pi*radius**2 #Defines Area            
	return Area

radius = 3
print(f"the result of the area of the circle, with radius = {3} is {Circle(radius)} cm^2")


def subtract(a, b): #gives both variables for all computations, and then uses all arithmetic 
	return b - a

b = 4 
a = 5
print(f"the result of the b - a, with a = {5} and b = {4} is {subtract(a, b)}")
def multiply (c, d):
	return c*d
c = 7
d = 6
print(f"the result of the c*d, with c = {7} and d = {6} is {multiply (c, d)}")
def divide (e, f):
	return e/f

e = 100
f = 34
print(f"the result of the e/f, with e = {100} and f = {34} is {divide (e, f)}")


def Temperature_ranges(readings):
	 #examples of temperatures you could be using
	return min(readings), max(readings)#then using the min and max commands you can find the temps you care about in the list

readings = [27, 14, 3, 11, 9]
print(f"the result of the temperature checking, with readings = [{27}. {14}, {3}, {11}, {9}] is {Temperature_ranges(readings)}")


def is_weekday(day):
	if day == 7 or day == 6: #since we know that 6 and 7 are the weekend we can just use if day = 6 / 7 then we know its the weekend
		weekend_checker = True
	else: #then use else if its anything else than a weekend
		weekend_checker = False
	return(weekend_checker)

day = 5
print(f"the result of the weekend checker, with day = {5} is {is_weekday(day)}")

def Fuel_Effeciency(Effeciency):
#we know that to find Eff it's gonna be the miles per gallon or miles/gallon
	Eff = miles/gallon #this will be our equation for Eff
	return (Eff)

def Encryption(input):
	remainder = input % 10 #We get 12345 then => 5 cause thats the decimal  
	Whole_number = input // 10 #then we get the rest of the number: 1234 after dividing by 10 then removing the decimal 
	encryption_one = remainder * 10 ** len(str(Whole_number))#This will give us 50000
	encryption_final = encryption_one + Whole_number #50000 + 1234 = 51234
	return(encryption_final)

input = 2468
print(f"the result of the super astronomy encryption system is, with our input being = {2468} is {Encryption(input)}")

def return_function(x, y): 
	value = 1 #define our value as 1 to adhere to the law of exponents
	for number in range(y): #this shows the numbers inside of y knowing how much to multiply it by
		value = value * x # then this multiplies the number of y values by x, y times. 
	return value

x = 8
y = 5
print(f"the result of the exponent maker system which is x = {8} a y = {5} is {return_function(x, y)}")

def loop_min(list):
	#Given a list of this sort, for every value in the list, we'll check with an if or else statement to see each number
	min_value = list[0] #asign min value as nothign so it'll always be replaced
	for value in list: #This will go through as many times theres a value in the list
		if value < min_value: #checks each value for the lowest possible value and then sets it equal to the lowest value no matter what
			min_value = value
	return min_value
list = [39, 12, 4]
print(f"the result of the minimum values using a for loop, which uses list = [{39}, {12}, {4}] is {loop_min(list)}")

def loop_max(list):
	max_value = list[0]#assigning nothing
	for value in list:#repeats for every thing in the list #number of times
		if max_value < value: #then goes thorugh every highest value and then prints it out
			max_value = value
	return max_value
	
list = [2, 745, 3]
print(f"the result of the maximum values using a for loop, which uses list = [{2}, {745}, {3}] is {loop_max(list)}")
	
def while_loop_min(list):
	min_value = list[0]
	x = 1 #we set a pre-variable to make sure we can scale somethgin while using a while loop
	while x < len(list): #then while that variable is smaller than the value of the list, it'll keep repeating, going through each 
		if list[x] < min_value: #checks if the specific value of the list is smaller, and then goes through every single input of the lsit to find the lowest value
			min_val = list[x]
		x = x + 1 #after the loop, it'll increase the pre-variable to make sure it'll check every list entry one at a time
	return min_val

list = [23, 6, 23,]
print(f"the result of the minimum value using a while loop, which uses list = [{23}, {6}, {23}] is {while_loop_min(list)}")

def while_loop_max(list):
	max_value = list[0]
	x = 1 #same pre-determined variable in order to scale through the entire list
	while x < len(list): #makes suer it goes through the whole list by stopping when x is bigger than the list
		if list[x] > max_value:#checks for each value and sees if its bigger than the others
			max_value = list[x]#then sets the biggest value and returns it, afterwards increasing the variable to make sure the loop isn't infinite
		x = x + 1
	return max_value

list = [3, 23, 765]
print(f"the result of the max value using a while loop, which uses list = [{2}, {23}, {765}] is {while_loop_max(list)}")

def sum_calulator(value):
	total = 0 #setting the total to nothing making sure the sum doens't get scruffed with a 1 or random variable
	for value in str(value): #making the value into a strand to be able to split it up
		total = total + int(value) #then going through each value in the strand, then adding it individually to the total
	return total #return said total
value = 879
print(f"the result of the sum calculator, which uses a value = {879} is {sum_calulator(value)}")

#my faovirte function is gonna be the Fuel Efficency question:
def Fuel_Effeciency(miles, gallons):
#we know that to find Eff it's gonna be the miles per gallon or miles/gallon
	Eff = miles/gallons #this will be our equation for Eff
	return (Eff)

gallons = 2
miles = 30
result = Fuel_Effeciency(miles, gallons) #Effeciency = 30/2 
print(f"the result of the fuel efficiency calculator (5.3), with gallons = {2} and miles = {30} is {result} percent fuel efficiency")