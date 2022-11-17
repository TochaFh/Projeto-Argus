from routeInterpreter import RouteInterpreter

route = RouteInterpreter("F10,D90,F40,D90,P5,C1,F10,D90,F40,C0,D90,A0,F5")

if not route.isValid():
    print("***************************")
    print("Código de rota inválido")
    print(route.errorMessage)
    print("***************************")
    exit(2)

for c in route.getCommands():
    c.PRINT()