print("Ejercicio 1");
n = (0,1,2,3,4,5,6,7); #otra forma de hacerlo
for num in n:
    print(num);

for n in range(1,13):  #forma de a hacerlo
    print(n);

print("Ejercicio 3");
for n in range(3,100,3):
    print(n);

print("Ejercicio 4");
for n in range(10,0,-1):
    print(n);
print("Despegue")

print("Ejercicio 5");
from turtle import *
for n in range(4):
    forward(50)
    right(90)