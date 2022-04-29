import math
import numpy as np
from math import radians
num_1 = int (input ("Please enter the first number: "))
calc = input("Please enter calc (+,-,*,/,/*,**,sin,cos,tan,sinh,tanh,cosh,asin,acos,atan,asinh,accosh,atanh,log,exp,sqrt,degrees,radians,factorial,cbrt): ")    

if calc in ('+','-','*','/','/*','**'): 
    num_2 = int (input ("Please enter the second number: "))
    
if calc == '+':
        print (num_1, " + ", num_2, " = ", num_1+num_2)
elif calc == '-':
        print (num_1, " - ", num_2, " = ", num_1-num_2)     
elif calc == '*':
        print (num_1, " * ", num_2, " = ", num_1*num_2)    
elif calc == '/':
    print (num_1, " / ", num_2, " = ",num_1/num_2)   
elif calc == '/*':
    print (num_1, " / ", num_2,"*",100, " = ",num_1/num_2*100) 
elif calc == '**':
    print (num_1, " ** ", num_2, " = ",num_1**num_2)  
elif calc=='sin':
    print(math.sin(radians(num_1)))
elif calc=='cos':
    print(math.cos(radians(num_1)))
elif calc=='tan':
    print(math.tan(radians(num_1)))
elif calc=='sinh':
    print(math.sinh(radians(num_1)))
elif calc=='tanh':
    print(math.tanh(radians(num_1)))
elif calc=='cosh':
    print(math.cosh(radians(num_1)))
elif calc=='asin':
    print(math.asin(radians(num_1)))
elif calc=='acos':
    print(math.acos(radians(num_1)))
elif calc=='atan':
    print(math.atan(radians(num_1)))
elif calc=='asinh':
    print(math.asinh(radians(num_1)))
elif calc=='acosh':
    print(math.acosh(radians(num_1)))
elif calc=='atanh':
    print(math.atanh(radians(num_1)))
elif calc=='log':
    print(math.log(num_1))
elif calc=='exp':
    print(math.exp(num_1))
elif calc=='sqrt':
    print(math.sqrt(num_1))
elif calc=='degrees':
    print(math.degrees(num_1))
elif calc=='radians':
    print(math.radians(num_1))
elif calc=='factorial':
    print(math.factorial(num_1))
elif calc=='cbrt':
    print(np.cbrt(num_1))
else:    
   print ("This is an invalid input") 