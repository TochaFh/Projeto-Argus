import tkinter
import Config
import time
from Config import motorLeft, motorRight

def stopMotors():
    motorLeft.stop()
    motorRight.stop()
def goLeft():
    motorLeft.stop()
    motorRight.run()
def goRight():
    motorLeft.run()
    motorRight.stop()
def go():
    motorLeft.run()
    motorRight.run()

# Lista das possíveis teclas de input com a informação se estão ou não pressionadas.
pressed = {
    'Up': False,
    'Down': False,
    'Right': False,
    'Left': False,
    'w': False,
    's': False,
    'd': False,
    'a': False,
    'space':False
}
entry_keys = pressed.keys()

# É chamada sempre que uma tecla é pressionada / está sendo pressionada.
def press_handler(event):
    #print(event.keysym + ' pressed')
    if event.keysym in entry_keys:
        if not pressed[event.keysym]:
            pressed[event.keysym] = True
            #print(event.keysym + ' pressed')
            update()

# É chamada sempre que uma tecla que estava sendo pressionada é solta.
def release_handler(event):
    if event:
        if event.keysym in entry_keys:
            pressed[event.keysym] = False
            #print(event.keysym + ' released')
            update()

# O update é chamado quando há mudança de estado. Faz a interpretação dos comandos.
# 0 = Stop, 1 = Go Forward, 2 = Go Backward, 3 = Rotate Right, 4 = Rotate Left, 5 = Turn Right Forward, 6 = Turn Left Forward, 7 = Turn Right Backward, 8 = turn Left Backward
def update():
    up = pressed['Up'] or pressed['w']
    stop = pressed['Down'] or pressed['s'] or pressed['space']
    right = pressed['Right'] or pressed['d']
    left = pressed['Left'] or pressed['a']

    if up:
        print("Frente")
        go()
        Config.buzz(0.5)
    elif right:
        print("Direita")
        goRight()
    elif left:
        print("Esquerda")
        goLeft()
    elif stop:
        print("Parou!")
        stopMotors()

# Envia o código para o robô via Bluetooth.
def send(msg: bytes):
    pass

# Cria uma janela no sistema operacional para receber o input do teclado.
r = tkinter.Tk()
r.title("Blackstorm")
r.geometry('400x200')
label = tkinter.Label(r, text = "ARGUS\nControle do robô\nAtivo")
label.pack()

# Cadastra os eventos de tecla pressionada e solta.
r.bind('<KeyPress>', press_handler)
r.bind('<KeyRelease>', release_handler)

# Faz a mágica acontecer :D
print("O controle está ativo")
r.mainloop()

print("Programa encerrado.")
stopMotors()