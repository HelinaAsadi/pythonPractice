# VARIABLES : container for vales. 4 types of variables are string, integer, float, boolean

# strings
first_name = "Helina"
last_name = 'Asadi'

print(first_name)
 # using f string to pring a combo of given texts and variables
print(f"Hello there {first_name} {last_name}")


# itegers (whole numbers)
age = 20

# float (floating point numberwith a decimal proportion)
distance_to_dreams = 1090373093900373191.9729


#boolean
happy = False
depressed = True
if happy :
    print("yaaaay :)")
else:
    print("poor you :(")

#####################################################
# DataTypes

name = "Helina"
age = 20
gpa = 3.7
student = True

# to get the datatype of a variable
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# TypeCasting

# explicitly
float_age = float(age)
print(float_age)

int_gpa = int(gpa)
print(int_gpa)

str_student = str(student)
print(str_student)

# to check to see if entries are not null
bool_age = bool(age) # anything but zero will cast to "True"
print(bool_age)


# implicitly

x = 2
y = 2.0

z = x/y
print(type(z))


########################################
# if statement is used for implementing decision making by checking if a condition is True or not

time = int(input("what time is it? (0 to 24)")) # user input is always string

if (time <= 2) or (time>=22) :
    print("GO GET SOME FUCKING SLEEP")
elif time > 2 and time <7:
    print("it's hopeless")
else:
    print("keep grinding I guess")

tired = input("are you tired? (y/n)")
if tired == "y": # == is used for comrison
    print("again HOPELESS")
else:
    print("side eye")

always = True
if always:
    print("poor you")



####################################
# while loops ; used for executing code as long as a condition is True

name = input("what is your name?")

while name =="":
    print("i am waitig!")
    name = input("?") # without ti code will continue executig nonstop

print(f"well hi {name}")

food = input("what is your favorite food? (quit)")
while not food =="quit":
    print(f"me too :)")
    food = input("what else?")

print("ok bye")
