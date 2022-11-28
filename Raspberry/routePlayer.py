from routeInterpreter import RouteInterpreter
from motor import Motor
import time

class RoutePlayer:
    def __init__(self, route: RouteInterpreter, motorRight: Motor, motorLeft: Motor):
        self.route = route
        self.motorRight = motorRight
        self.motorLeft = motorLeft

        self.turnDivisor = 50

    def stopMotors(self):
        self.motorRight.stop()
        self.motorLeft.stop()
            
    def play(self):
        for c in self.route.commands:

            if c.type == 'F':
                self.motorRight.regularSpeed()
                self.motorLeft.regularSpeed()

                for step in range(c.value):
                    # cada passo tem um sgundo de duração
                    time.sleep(1)

                    # aqui vem o código de segurança que faz o robô parar caso o sensor ultassônico detecte algo na frente
                    # a ideia inicial é fazer essa checagem uma vez por segundo

                self.stopMotors()

            if c.type == 'D':
                self.motorRight.stop()
                self.motorLeft.fast()

                # o valor estará em graus, será necessário testes para definir um número que dividirá o
                # valor em graus resultando no numero de segundos em que o robô ficará virando
                time.sleep(float(c.value) / self.turnDivisor)
                self.stopMotors()

            if c.type == 'E':
                self.motorRight.stop()
                self.motorLeft.fast()

                # o valor estará em graus, será necessário testes para definir um número que dividirá o
                # valor em graus resultando no numero de segundos em que o robô ficará virando
                time.sleep(float(c.value) / self.turnDivisor)
                self.stopMotors()