from usuario_credito import *

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjetas = [] 

    def agregar_tarjeta(self, tarjeta):
        if isinstance(tarjeta, TarjetaCredito):
            self.tarjetas.append(tarjeta)
            print(f"Se agregó una nueva tarjeta al usuario {self.nombre}.")
        else:
            print("La tarjeta indicada no existe")
            
    def hacer_compra(self, monto, tarjeta):
        if tarjeta in self.tarjetas:
            tarjeta.compra(monto)
            return self
        else:
            print("Tarjeta no encontrada en el usuario")
            return self

    def pagar_tarjeta(self, monto, tarjeta):
        if tarjeta in self.tarjetas:
            tarjeta.pago(monto)       
        else:
            print("Tarjeta no encontrada en el usuario")
            
    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo total por tarjeta:")
        for tarjeta in self.tarjetas:
            tarjeta.mostrar_info_tarjetas()
    
    def transferir_deuda(self, otro_usuario, monto, tarjeta_origen, tarjeta_destino):
        if tarjeta_origen in self.tarjetas and tarjeta_destino in otro_usuario.tarjetas:
            if monto <= tarjeta_origen.saldo_pagar:
                tarjeta_origen.saldo_pagar -= monto
                tarjeta_destino.saldo_pagar += monto
                print(f"Transferidos ${monto} de {self.nombre} a {otro_usuario.nombre}")
            else:
                print("Monto mayor al saldo de la tarjeta origen.")
        else: 
            print("Alguna de las tarjetas no pertenece a su usuario correspondiente")


usuario1 = Usuario("Manuel", "Orellana", "manuel@gmail.com")
usuario2 = Usuario("Jose", "Cabrera", "jose@gmail.com")

mastercard = TarjetaCredito(12000, 0.02)
visa = TarjetaCredito(10000, 0.02)

usuario1.agregar_tarjeta(mastercard)
usuario1.agregar_tarjeta(visa)
usuario1.hacer_compra(2000, mastercard)
usuario1.hacer_compra(1000, visa)
usuario1.mostrar_saldo_usuario()

visa2 = TarjetaCredito(15000, 0.03)  # Nuevo nombre para no reemplazar visa anterior
usuario2.agregar_tarjeta(visa2)
usuario2.hacer_compra(3000, visa2)
usuario2.mostrar_saldo_usuario()

# Transferencia del BONUS
usuario1.transferir_deuda(usuario2, 500, mastercard, visa2)
usuario1.mostrar_saldo_usuario()
usuario2.mostrar_saldo_usuario()
