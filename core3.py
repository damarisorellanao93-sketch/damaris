class TarjetaCredito:
    todas_las_tarjetas = []

    def __init__(self, limite_credito=5000, intereses=0.03):
        self.saldo_pagar = 0
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.todas_las_tarjetas.append(self)  #Agregar a la lista general

    #El usuario realiza una compra
    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, alcanzó su límite de crédito.")
        return self

    #El usuario realiza un pago
    def pago(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar = 0
        return self

    #Cobra intereses sobre el saldo actual
    def cobrar_intereses(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    #Muestra la información de la tarjeta
    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        return self

    #bonus, mostrar todas las tarjetas creadas
    @classmethod
    def mostrar_todas(cls):
        print("Información de todas las tarjetas")
        for tarjeta in cls.todas_las_tarjetas:
            tarjeta.mostrar_info_tarjeta()

#Realiza 2 compras, realiza 1 pago, cobra intereses y muestra la información de la tarjeta
tarjeta1 = TarjetaCredito(limite_credito=5000, intereses=0.03)
tarjeta1.compra(500).compra(200).pago(300).cobrar_intereses().mostrar_info_tarjeta()

#Realiza 3 compras, realiza 2 pagos, cobra intereses y muestra información de la tarjeta
tarjeta2 = TarjetaCredito(limite_credito=5000, intereses=0.03)
tarjeta2.compra(200).compra(500).compra(400).pago(400).pago(500).cobrar_intereses().mostrar_info_tarjeta()

#Realiza 5 compras que exceden el límite y muestra información de la tarjeta
tarjeta3 = TarjetaCredito(limite_credito=5000, intereses=0.03)
tarjeta3.compra(1000).compra(1500).compra(1000).compra(1500).compra(500).mostrar_info_tarjeta()

#Bonus, mostrar todas las tarjetas
TarjetaCredito.mostrar_todas()
