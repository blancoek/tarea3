class BilleteraElectronica:

    def __init__(self, identificador, nombres, apellidos, CI, PIN):
        self.identificador=identificador
        self.nombres=nombres
        self.apellidos=apellidos
        self.CI=CI
        self.PIN=PIN
        self.recargas=[]
        self.consumos=[]
        self.balance=0
        
    def saldo(self):
        return self.balance
    
    def recargar(self,nuevarecarga):
        if (nuevarecarga.monto>0):
            self.recargas.append(nuevarecarga)
            self.balance=self.balance+nuevarecarga.monto
        else:
            print("No puede haber una recarga negativa")

    def consumir(self,nuevoconsumo,PIN):
        if (PIN==self.PIN):
            if (self.saldo()>nuevoconsumo.monto):
                if (nuevoconsumo.monto>0):
                    self.consumos.append(nuevoconsumo)
                    self.balance=self.balance-nuevoconsumo.monto
                else:
                    print("No puede haber un consumo negativo")
            else:
                print("Saldo Insuficiente")
        else:
            print("PIN Erroneo")