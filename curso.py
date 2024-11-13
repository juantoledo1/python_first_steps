# print("hola mundo como estan estoy practicando python Y ESOTY MUY FELIZ")
# x = 10
# c = 55
# #vamos a robar la suma ahora

# print(x + c)

# nombre = "juan"
# apellido =  "toledo"
    
# print(f"hola mi nombre de usuario es {nombre} y mi apellido es {apellido}")

# x = 3 + 1j
# print (x)

# nombre = input("cual es tu nombre completo: ")
# edad= int(input("cual es tu edad: "))
# altura= float(input("cual es tu altura exacta: "))

# print(f"hola mi nombre es: {nombre} mi edad es: {edad} mi altura exacta es: {altura}")





#operadores aritmeticos

# a = 10
# b = 5

# suma = a + b
# resta = a - b
# multiplicacion = a * b
# division = a / b
# division_entera = a // b
# modulo = a % b
# potencia = a ** b

# print (suma, resta, multiplicacion, division, division_entera, modulo, potencia)

# #variables de comparacion 

# c = 20

# es_mayor = a > c
# es_menor_o_igual = b < c
# es_igual = a == b
# no_es_igual = a != c

# print(es_mayor, es_menor_o_igual, es_igual, no_es_igual)







# #operadores logicos    
# d = True
# e = False
# and_logico = d and e
# or_logico =  d or e
# not_logico = not d

# print(and_logico, or_logico, not_logico)


#operadores ede asignacion
# f = 5
# f += 2
# f -= 1
# f *= 3
# f /= 2
# f %= 4
# f //= 2
# f **= 3


#operadores de identidad
# g = 10
# h = g

# son_el_mismo_objeto = g is h
# no_son_mismo_objeto = g is not h

# print(son_el_mismo_objeto, no_son_mismo_objeto)



#ejercicio
# supongamos que eres el dueño de una verduleria y quieres crear un programa que te permita 
# calcular el precio  total de una compra de frutas.
# cada fruta tiene un precio diferente y los clientes pueden comprar varias frutas a la vez.
# Para ello utiliza operadores aritmeticos y de asignacion.

precio_manzana = 10
precio_banana =  5
precio_naranja = 10.50
precio_pera = 12.20


#cantidad e frutas que se quiere
m = int(input("indique cuantas manzanas quiere: "))
b = int(input("indique cuantas bananas quiere: "))
n = int(input("indique cuantas naranjas quiere: "))
p = int(input("indique cuantas peras quiere: "))

#calculo de percio y cantidad
total =0
total += m * precio_manzana
total += b * precio_banana
total += n * precio_naranja
total += p * precio_pera

#total de la compra

print(f"el total de la compra es {total:.2f}")
