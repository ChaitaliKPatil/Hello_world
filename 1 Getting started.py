#Q1
# Hash is used for writing comments here.
# This is start of the course and thus the code writing.
print('Q1\nHello world')
print('Hi Manu')
print ('Hi Chinu\n\n\n\n')


#Q2
# attempt to display Escape Sequences
# single, double codes, backslash, backspace, new line, Tab.
print('Q2\nLine A \\n Line B')
print('\\\" \n\\\'\n\n\n\n')
# Obtaining User Input and then storing the input value to a variable using = Operator


#Q3
#Declaring and Assigning values to variables
a=8
print('Q3\nValue of a',a)
b=10
print('Value of b after assigning the value',b)
c=a+b
print('Value of c after adding a and b',c)
a=b=c=20
print('New value of c',c)
a,b,c=4,5,6
print('array value of a',a)
print('array value of b',b)
print('array value of c',c,'\n\n\n\n')
# Something like an array separated with comma get the values specifically.


#Q4
Age= input('Q4\nWhat is your age?')
print('My age is', Age)
print('My','age','is',Age)# Here comma gives a single space after each listed element.
print('My','age','is',Age,sep='*',end='!\n') 
print('My','age','is',Age,sep='^',end='!') 
# Here Any element listed in SEP separates all the listed elements by the element in SEP. 
# END in the list displays the character at the end of the list, as ! here.
# \n adds new line after the current.