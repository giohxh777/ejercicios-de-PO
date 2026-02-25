from cocina import Cocina
from ingredientes import Tomate, Cebolla, Pasta
from cuchillo import Cuchillo
from olla import Olla


print("ESTACIÓN DE BATALLA: COCINA\n")

cocina = Cocina()
cocina.verificar_ingredientes()


tomate = Tomate("Tomate", 100, "Crudo")
cebolla = Cebolla("Cebolla", 100)
pasta = Pasta("Pasta")


cuchillo = Cuchillo("Samurai", 100)


olla = Olla()


while cebolla.get_vida() > 0:

    print("\n1. Cortar Cebolla")
    print("2. Afilar Cuchillo")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        cuchillo.hacer_corte(cebolla)

    elif opcion == "2":
        cuchillo.afilar()

    else:
        print("Opción inválida")


while tomate.get_vida() > 0:

    print("\n1. Cortar Tomate")
    print("2. Afilar Cuchillo")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        cuchillo.hacer_corte(tomate)

    elif opcion == "2":
        cuchillo.afilar()

    else:
        print("Opción inválida")


tomate.cambiar_estado("Picado")

print("\nIngredientes vencidos. Pasando a la olla...\n")

olla.agregar(cebolla)
olla.agregar(tomate)


print("\nprende la pasta y comienza a hervir")

while pasta.get_coccion() < 100:

    print(f"Cocción actual: {pasta.get_coccion()}%")
    seguir = input("¿Deseas seguir hirviendo? (si/no): ")

    if seguir.lower() == "si":
        pasta.hervir()

    elif seguir.lower() == "no":
        print("La pasta quedó cruda. Juego terminado.")
        break

    else:
        print("Opción inválida")


if pasta.get_coccion() == 100:
    print("\nCombate culinario finalizado")

    print("La pasta ha sido servida con éxito.")
