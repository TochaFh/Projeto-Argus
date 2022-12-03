from time import strftime
from routeInterpreter import RouteCommand
import time
import os

class Photographer:
    def __init__(self, name: str, directory: str):
        self.name = name
        self.directory = directory + "/" + name
        os.mkdir(self.directory)

    def takePhoto(self, com: RouteCommand, step: int):
        location = "Comando-" + str(com.position) + ":" + com.TEXT() + "-Passo-" + str(step)
        photo = Photo(self, strftime("%I-%M%p"), location)
        
        imgName = photo.INFO()
        os.system("fswebcam -r 640x480 --no-banner " + self.directory + "/" + imgName + ".jpg")
        
        print(imgName)

    def NAME(self):
        return self.name

class Photo:
    def __init__(self, photographer: Photographer, time: str, location: str):
        self.photographer = Photographer
        self.time = time
        self.location = location
        self.info = time + "-" + location
    
    def INFO(self):
        return self.info