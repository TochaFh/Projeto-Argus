from time import strftime
from routeInterpreter import RouteCommand

class Photographer:
    def __init__(self, name: str):
        self.name = name

    def takePhoto(self, com: RouteCommand, step: int):
        location = "Comando " + str(com.position) + ": " + com.TEXT() + " - Passo " + str(step)
        photo = Photo(self, strftime("%d/%m/%y at %I:%M%p"), location, "untitled")
        print("FOTO TIRADA!")
        print(photo.INFO())

    def NAME(self):
        return self.name

class Photo:
    def __init__(self, photographer: Photographer, time: str, location: str, fileName: str):
        self.photographer = Photographer
        self.time = time
        self.location = location
        self.info = "Foto de" + photographer.NAME() + " - " + time + " - " + location
    
    def INFO(self):
        return self.info