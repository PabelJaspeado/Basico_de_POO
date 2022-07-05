from dogs import Dogs

class SmallestDogs(Dogs):
    typesize = []

    def __init__(self, name, age, breed, typesize):
        super().__init__(name, age, breed)
        self.typesize = typesize