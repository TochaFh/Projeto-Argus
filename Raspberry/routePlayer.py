from routeInterpreter import RouteInterpreter
from motor import Motor
from photographer import Photographer
#from Startup import BUZZER
import RPi.GPIO as GPIO
import time

class RoutePlayer:
    def __init__(self, route: RouteInterpreter, motorLeft: Motor, motorRight: Motor, photographer: Photographer):
        self.route = route
        self.motorLeft = motorLeft
        self.motorRight = motorRight
        self.photographer = photographer
        self.capture = 0

        self.turnDivisor = 45

    def stopMotors(self):
        self.motorLeft.stop()
        self.motorRight.stop()
            
    def play(self):
        for i, c in enumerate(self.route.commands):

            if c.type == 'F': # FRENTE
                self.motorLeft.run()
                self.motorRight.run()
                print("Executando: " + c.NAME())

                for step in range(c.value):
                    # cada passo tem um sgundo de duração
                    time.sleep(1)
                    # aqui vem o código de segurança que faz o robô parar caso o sensor ultassônico detecte algo na frente
                    # a ideia inicial é fazer essa checagem uma vez por segundo

                    if self.capture == 1:
                        self.photographer.takePhoto(c, step)

                self.stopMotors()

            elif c.type == 'D': # DIREITA
                self.motorLeft.run()
                self.motorRight.stop()
                print("Executando: " + c.NAME())

                # o valor estará em graus, será necessário testes para definir um número que dividirá o
                # valor em graus resultando no numero de segundos em que o robô ficará virando
                'time.sleep(float(c.value) / self.turnDivisor)'

                # por enquanto testaremos com o valor em segundos
                time.sleep(c.value)
                self.stopMotors()

            elif c.type == 'E': # ESQUERDA
                self.motorLeft.stop()
                self.motorRight.run()
                print("Executando: " + c.NAME())

                # o valor estará em graus, será necessário testes para definir um número que dividirá o
                # valor em graus resultando no numero de segundos em que o robô ficará virando
                'time.sleep(float(c.value) / self.turnDivisor)'

                # por enquanto testaremos com o valor em segundos
                time.sleep(c.value)
                self.stopMotors()
                
            elif c.type == 'P': # PARAR
                self.stopMotors()
                print("Executando: " + c.NAME())
                
                if c.value == 0:
                    # na versão final, o robô ficará "pausado" até que um botão seja pressionado ou
                    # um sinal bluetooth seja recebido
                    print("Parando P0")
                    #GPIO.output(BUZZER, GPIO.HIGH)
                    #time.sleep(2)
                    #GPIO.output(BUZZER, GPIO.LOW)
                    time.sleep(3)
                else:
                    time.sleep(c.value)
            
            elif c.type == 'C':
                # Este comando ativará/desativará a função de captura de imagens
                print("Executando: " + c.NAME())

                #GPIO.output(BUZZER, GPIO.HIGH)
                #time.sleep(0.3)
                #GPIO.output(BUZZER, GPIO.LOW)
                #time.sleep(0.3)
                #GPIO.output(BUZZER, GPIO.HIGH)
                #time.sleep(0.5)
                #GPIO.output(BUZZER, GPIO.LOW)
                
                self.capture = c.value