from account import Account
from buyer import Buyer
from seller import Seller
from dogs import Dogs
from smallestDogs import SmallestDogs

def main():
    tamaño_de_perro = input("¿Cuál es el tamaño de perro que buscas? (Pequeño, Mediano, Grande) ")
    if tamaño_de_perro == "Pequeño":
        return
    else:
         print("Por el momento no tenemos ese tamaño de perro")

if __name__ == "__main__":
    main()

    print("Usuario: ")
    usuario = Account("Juan Perez", "juanito@hotmail.com", "12345")
    print(vars(usuario))

    print("Tienda: ")
    tienda = Seller("Adopta a tu amigo ideal", "adopta.tu.amigo.ideal@hotmail.com", "3646afaf")
    print(vars(tienda))
    
    print("Perro pequeño: ")
    perropequeño = SmallestDogs("Fido", 2, "Chihuahua", "Pequeño")
    print(vars(perropequeño))

