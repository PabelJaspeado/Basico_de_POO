from dogs import Dogs

class MediumSizedDogs(Dogs):
    typesize = []

    def __init__(self, name, age, breed, typesize):
        super().__init__(name, age, breed)
        self.typesize = typesize
       