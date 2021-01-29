#print(5 < 10)
#print(2 > 20)
#print(6 <= 6)
#print(0 == 0)

'''
promedio = input("Pedir Promedio")
si promedio > 6 entonces
	aprueba
sino
	reprueba
'''

num1 = int(input("Pedir primera nota:"))
num2 = int(input("Pedir segunda nota:"))
num3 = int(input("Pedir tercera nota:"))

promedio = (num1 + num2 + num3)/3

print("El promedio es %.2f"%promedio)

if(promedio > 6):
	print("Aprobado")
else:
	print("Desaprobado")