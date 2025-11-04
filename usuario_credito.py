class TarjetaCredito:
    
    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.limite_credito = limite_credito
        self.intereses = intereses
        self.saldo_pagar = saldo_pagar
    
    def compra(self, monto):
        total = self.saldo_pagar + monto
        if (total > self.limite_credito):
            print("Tarjeta Rechazada, has alcanzado tu limite de crédito")
            return self
        else:
            self.saldo_pagar += monto
        return self
    
    def pago(self, monto):
        if (monto > self.saldo_pagar):
            print("El monto ingresado supera el saldo a pagar")
            self.mostrar_info_tarjetas()
            return self
        else:
            self.saldo_pagar -= monto
        return self
        
    def mostrar_info_tarjetas(self):
        print(f"El saldo a pagar es: {self.saldo_pagar}")
        return self
        
    def cobrar_intereses(self):
        intereses_a_pagar = self.saldo_pagar * self.intereses
        self.saldo_pagar += intereses_a_pagar
        return self


#tarjeta1
tarjeta1 = TarjetaCredito(10000, 0.02, 100)
tarjeta1.compra(4000).compra(1000).pago(4000).cobrar_intereses().mostrar_info_tarjetas()

#tarjeta2
tarjeta2 = TarjetaCredito(12000, 0.03)
tarjeta2.compra(2000).compra(1000).compra(1600).pago(3000).pago(1500).cobrar_intereses().mostrar_info_tarjetas()

#tarjeta3
tarjeta3 = TarjetaCredito(11000, 0.02)
tarjeta3.compra(2000).compra(1000).compra(1600).compra(4000).compra(3000).cobrar_intereses().mostrar_info_tarjetas()
