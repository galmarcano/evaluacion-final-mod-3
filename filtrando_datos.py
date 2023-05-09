lista_original = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
lista_magos = [lista_original[nombre] for nombre in [0, 2, 5]]
lista_cientificos = [lista_original[nombre] for nombre in [1, 3, 6]]

lista_otros = []
for nombre in lista_original:
    if nombre not in lista_magos and nombre not in lista_cientificos:
        lista_otros.append(nombre)

def hacer_grandioso():
    for nombre in lista_magos:
        print(f"El gran {nombre}")

def imprimir_nombres():
    for nombre in lista_original:
        print(nombre)


print("Lista de nombres originales:")
imprimir_nombres()

print()

print("Lista de los magos grandiosos:")
hacer_grandioso()

print()

print("Lista de científicos:")
print("\n".join(lista_cientificos))

print()

print("Lista de nombres restantes:")
print("\n".join(lista_otros))