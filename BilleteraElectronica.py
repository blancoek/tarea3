class BilleteraElectronica:

    def __init__(self, identificador, nombres, apellidos, CI, PIN):
        self.identificador=identificador
        self.nombres=nombres
        self.apellidos=apellidos
        self.CI=CI
        self.PIN=PIN
        self.recargas=[]
        self.consumos=[]
        
    def saldo(self):
        abonado=0
        for recarga in self.recargas:
            abonado=abonado+recarga.monto
        deuda=0
        for consumo in self.consumos:
            deuda=deuda+consumo.monto
        return abonado-deuda
    
    def recargar(self,nuevarecarga):
        self.recargas.append(nuevarecarga)

    def consumir(self,nuevoconsumo,PIN):
        if (PIN==self.PIN):
            if (self.saldo>nuevoconsumo.monto):
                self.consumos.append(nuevoconsumo)
            else:
                print("Saldo Insuficiente")
        else:
            print("PIN Erróneo")