from photographer import Photographer
from routeInterpreter import RouteInterpreter
from routePlayer import RoutePlayer
from time import strftime
from motor import Motor
import os
import RPi.GPIO as GPIO
        
def teste_route_player(motorLeft: Motor, motorRight: Motor):
    route = RouteInterpreter("Teste,C1,F7")
    if not route.isValid():
        print("***************************")
        print("Código de rota inválido")
        print(route.errorMessage)
        print("***************************")
        exit(2)
    
    directory = "/home/argus/ImagesArgus/" + route.name + "--" + strftime("%d-%m-%y--%I-%M%p")
    os.mkdir(directory)
    
    print("Criando route player...")
    player = RoutePlayer(route, motorLeft, motorRight, Photographer("Esquerda", directory))
    
    print("-- Iniciando roteiro ")
    player.play()
    print("-- Fim do roteiro")

GPIO.setmode(GPIO.BCM)
motorLeft = Motor(23, 'Esquerda')
motorRight = Motor(24, 'Direita')
teste_route_player(motorLeft, motorRight)


def teste_route_interpreter():
    route = RouteInterpreter("TESTE 1,F10,D90,F40,D90,P5,C1,F10,D90,F40,C0,D90,P0,F5")

    if not route.isValid():
        print("***************************")
        print("Código de rota inválido")
        print(route.errorMessage)
        print("***************************")
        exit(2)

    for c in route.getCommands():
        c.PRINT()
    
def teste_motores(motorRight: Motor, motorLeft: Motor):
    for i in range(4):
        motorRight.run()
        motorLeft.stop()
        time.sleep(3)
        motorRight.stop()
        motorLeft.run()
        time.sleep(3)