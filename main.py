from account import Account
from seller import Seller
from smallestDogs import SmallestDogs
from mediumSizedDogs import MediumSizedDogs
from tallestDogs import TallestDogs

def main():
    tamaño_de_perro = input("¿Cuál es el tamaño de perro que buscas? (Pequeño, Mediano, Grande) ")
    if tamaño_de_perro == "Pequeño":
        print("Usuario: ")
        usuario = Account("Juan Perez", "juanito@hotmail.com", "12345")
        print(vars(usuario))

        print("Tienda: ")
        tienda = Seller("Adopta a tu amigo ideal", "adopta.tu.amigo.ideal@hotmail.com", "3646afaf")
        print(vars(tienda))
    
        print("Tu perro ideal es: ")
        perropequeño = SmallestDogs("Fido", 2, "Chihuahua", "Pequeño")
        print(vars(perropequeño))

    elif tamaño_de_perro == "Mediano":
        print("Usuario: ")
        usuario = Account("Juan Perez", "juanito@hotmail.com", "12345")
        print(vars(usuario))

        print("Tienda: ")
        tienda = Seller("Adopta a tu amigo ideal", "adopta.tu.amigo.ideal@hotmail.com", "3646afaf")
        print(vars(tienda))
    
        print("Tu perro ideal es: ")
        perromediano = MediumSizedDogs("Robert", 4, "Coker", "Mediano")
        print(vars(perromediano))

    elif tamaño_de_perro == "Grande":
        print("Usuario: ")
        usuario = Account("Juan Perez", "juanito@hotmail.com", "12345")
        print(vars(usuario))

        print("Tienda: ")
        tienda = Seller("Adopta a tu amigo ideal", "adopta.tu.amigo.ideal@hotmail.com", "3646afaf")
        print(vars(tienda))
    
        print("Tu perro ideal es: ")
        perrogrande = TallestDogs("Hermes", 1, "Husky", "Grande")
        print(vars(perrogrande))

    else:
         print("Por el momento no tenemos ese tamaño de perro")

if __name__ == "__main__":
    main()



