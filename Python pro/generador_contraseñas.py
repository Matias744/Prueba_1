import random

elementos = "0=+-.,¡123456789-abcdefghijklmnopqrstuvwxyz"
pass_lenght = int(input("Introduzcala longitud de su contraseña"))

password = ""

for i in range(pass_lenght):
    password += random.choice(elementos)
print("Contraseña generado:", password)