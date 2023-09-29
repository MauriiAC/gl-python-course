# Ejercicio POO

class Cliente():

    def __init__(self, nombre, apellido, edad, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__dni = dni
        self.__ticket = None

    def comprar_ticket(self, evento):
        self.__ticket = evento.generar_ticket(self.__dni)
        if self.__ticket:
            print(f'Su nro de ticket es {self.__ticket}')
        else:
            print('Ya no hay tickets disponibles!')
    
    def ingresar_evento(self, evento):
        if not self.__ticket:
            print('No posee ticket para este evento')
            return
        ingreso = self.__ticket.corroborar_ticket(self.__dni)
        if ingreso:
            print(evento.bienvenida())
        else:
            print(evento.rechazo())

class Evento():

    def __init__(self, numero, titulo, fecha, aforo):
        self.__numero = numero
        self.__titulo = titulo
        self.__fecha = fecha
        self.__aforo = aforo
        self.__siguiente_ticket = 1

    def generar_ticket(self, dni):
        if self.__aforo < self.__siguiente_ticket:
            return None
        else:
            nuevo_ticket = Ticket(self.__siguiente_ticket, dni)
            self.__siguiente_ticket += 1
            return nuevo_ticket
        
    def bienvenida(self):
        return f'Bienvenido a {self.__titulo}'

    def rechazo(self):
        return f'Usted no posee un ticket valido'

class Ticket():

    def __init__(self, numero, dni):
        self.__numero = numero
        self.__dni = dni
        self.__usado = False

    def corroborar_ticket(self, dni):
        if self.__usado == False and dni == self.__dni:
            self.__usado = True
            return True
        else: 
            return False
        
    def __str__(self):
        return str(self.__numero)
        
    
        
evento1 = Evento(1, "Final de Champions League", "2023-12-15", 5)

cliente1 = Cliente("Juan", "Martinez", 40, "123123")
cliente2 = Cliente("Juana", "Martinez", 23, "321321")
cliente3 = Cliente("Maria", "Martinez", 17, "010101")
cliente4 = Cliente("Adrian", "Martinez", 71, "111222")
cliente5 = Cliente("Martin", "Martinez", 51, "987789")
cliente6 = Cliente("Jose", "Martinez", 32, "333444")

cliente1.comprar_ticket(evento1)
cliente2.comprar_ticket(evento1)
cliente3.comprar_ticket(evento1)
cliente4.comprar_ticket(evento1)
cliente5.comprar_ticket(evento1)
cliente6.comprar_ticket(evento1)

cliente1.ingresar_evento(evento1)
cliente2.ingresar_evento(evento1)
cliente3.ingresar_evento(evento1)
cliente4.ingresar_evento(evento1)
cliente5.ingresar_evento(evento1)
cliente5.ingresar_evento(evento1)
cliente6.ingresar_evento(evento1)

