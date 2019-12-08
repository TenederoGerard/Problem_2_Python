from math import sqrt

x1 = int(input ('Enter value for x1=' ))
y1 = int(input ('Enter value for y1=' ))
x2 = int(input ('Enter value for x2=' ))
y2 = int(input ('Enter value for y2=' )) 
x3 = int(input ('Enter value for x3=' )) 
y3 = int(input ('Enter value for y3=' ))

#Equation for solving a circle passing through three points

A = x1*(y2-y3) - y1*(x2-x3) + (x2*y3) - (x3*y2)
B = (((x1**2) + (y1**2))*(y3-y2)) + (((x2**2) + (y2**2))*(y1-y3)) + (((x3**2) + (y3**2))*(y2-y1))
C = (((x1**2) + (y1**2))*(x2-x3)) + (((x2**2) + (y2**2))*(x3-x1)) + (((x3**2) + (y3**2))*(x1-x2))
G = (((x1**2) + (y1**2))*(((x3*y2) - (x2*y3)))) + (((x2**2)+(y2**2))*(((x1*y3) - (x3*y1)))) + (((x3**2) + (y3**2))*((x2*y1) - (x1*y2)))

#Center point (x,y) and radius of a circle passing through three points

x = -(B/ (2*A))
y = -(C/ (2*A))
r = sqrt(((B**2) + (C**2) - (4*A*G))/((4)*(A**2)))

#Vector D, E, F

D = B/A
E = C/A
F = G/A

Vector = [D, E, F]

print ('Center=(',x,',',y,')')
print ('Radius = %.2f'% r)
print ('Vector[D,E,F]=', Vector)

