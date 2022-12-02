from photographer import Photographer
from routeInterpreter import RouteInterpreter
from routePlayer import RoutePlayer
from motor import Motor

def teste_route_interpreter():
    route = RouteInterpreter("F10,D90,F40,D90,P5,C1,F10,D90,F40,C0,D90,P0,F5")

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
        
def teste_route_player(motorLeft: Motor, motorRight: Motor):
    route = RouteInterpreter("F10,D90,F5,D90,P5,C1,F10,D90,F5,C0,D90")
    if not route.isValid():
        print("***************************")
        print("Código de rota inválido")
        print(route.errorMessage)
        print("***************************")
        exit(2)
    print("Criando route player...")
    player = RoutePlayer(route, motorLeft, motorRight, Photographer("Fotógrafo Esquerda"))
    print("-- Iniciando roteiro")
    player.play()
    print("-- Fim do roteiro")