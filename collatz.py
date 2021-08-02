import numpy as np
import matplotlib.pyplot as plt

y_data = []



def collatzSequence(number):
    if (number % 2 == 0): # if it's even
        number = number // 2
        
    else:                 # if it's odd
        number = number * 3 + 1
       
    
    y_data.append(number,)
    return (number)

n = int(input('Enter a number: '))
y_data.append(n)
while (n != 1):
    
    n = collatzSequence(n)

z = len(y_data)
x_data = []


for i in range (1, z+1):
    x_data.append(i)



print (y_data)    
print(len(y_data))

plt.plot(x_data, y_data)

plt.show()