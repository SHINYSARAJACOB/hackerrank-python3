import math
AB=int(input())
BC=int(input())
x=AB*AB
y=BC*BC
z=x+y
AC=math.sqrt(z)
OC=(AC/2)

theta1=math.acos(BC/AC)
h = math.sin(theta1) * OC

THETA=math.asin(h/OC)
theta=math.degrees(THETA)
print("%d"u"\u00B0"%(round(theta)))