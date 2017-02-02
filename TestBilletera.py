from BilleteraElectronica import BilleteraElectronica
from classConsumos import Consumo
from classRecargas import Recarga
import datetime
import unittest
from datetime import date

class TestBilletera(unittest.TestCase):
    
    def testInit(self):
        identif=42
        nombres="Juan"
        apellidos="Gomez Castro"
        ci=20000000
        pin=1234
        billetera=BilleteraElectronica(identif,nombres,apellidos,ci,pin)
        self.assertEqual(identif, billetera.identificador)
        self.assertEqual(nombres, billetera.nombres)
        self.assertEqual(apellidos, billetera.apellidos)
        self.assertEqual(ci, billetera.CI)
        self.assertEqual(pin, billetera.PIN)
        self.assertEqual([], billetera.consumos)
        self.assertEqual([], billetera.recargas)
        self.assertEqual(0, billetera.balance)
        
    def testSaldo(self):
        saldo=0
        billetera=BilleteraElectronica(42,"Juan","Gomez Castro",20000000,1234)
        self.assertEqual(saldo, billetera.balance)
    
    def testRecargaInit(self):
        monto=20
        fecha=datetime.date.today()
        establecimiento="Sambil"
        recarga=Recarga(monto,fecha,establecimiento)
        self.assertEqual(recarga.monto,monto)
        self.assertEqual(recarga.fecha,fecha)
        self.assertEqual(recarga.establecimiento,establecimiento)

    def testConsumoInit(self):
        monto=20
        fecha=datetime.date.today()
        establecimiento="El Rodeo"
        consumo=Consumo(monto,fecha,establecimiento)
        self.assertEqual(consumo.monto,monto)
        self.assertEqual(consumo.fecha,fecha)
        self.assertEqual(consumo.establecimiento,establecimiento)
        
    def testRecargar(self):
        monto=50
        fecha=date(2007,12,5)
        establecimiento="Rubios"
        recarga=Recarga(monto,fecha,establecimiento)
        billetera=BilleteraElectronica(42,"Juan","Gomez Castro",20000000,1234)
        billetera.recargar(recarga)
        self.assertGreaterEqual(billetera.balance, monto)
    
    def testRecargarNegativo(self):
        monto=-50
        fecha=date(2007,12,5)
        establecimiento="McDolans"
        recarga=Recarga(monto,fecha,establecimiento)
        billetera=BilleteraElectronica(42,"Juan","Gomez Castro",20000000,1234)
        billetera.recargar(recarga)
        self.assertGreaterEqual(billetera.balance, monto)
    
    def testRecargarNulo(self):
        monto=0
        fecha=datetime.date(2011,11,11)
        establecimiento="FCK"
        recarga=Recarga(monto,fecha,establecimiento)
        billetera=BilleteraElectronica(42,"Juan","Gomez Castro",20000000,1234)
        billetera.recargar(recarga)
        self.assertGreaterEqual(billetera.balance, monto)
    
    def testConsumir(self):
        monto=50
        fecha=datetime.date.today()
        establecimiento="Artorus"
        consumo=Consumo(monto,fecha,establecimiento)
        billetera=BilleteraElectronica(100,"Pepito","Perez",10000000,6969)
        PIN=6969
        fechar=datetime.date(2007,12,5)
        billetera.recargar(Recarga(1000,fechar,"Sambil"))
        billetera.consumir(consumo,PIN)
        self.assertEqual(billetera.PIN,PIN)
        self.assertGreaterEqual(billetera.balance, monto)
        self.assertGreater(monto,0)

    def testConsumirNegativo(self):
        monto=-50
        fecha=datetime.date.today()
        establecimiento="Artorus"
        consumo=Consumo(monto,fecha,establecimiento)
        billetera=BilleteraElectronica(100,"Pepito","Perez",10000000,6969)
        PIN=6969
        fechar=datetime.date(2007,12,5)
        billetera.recargar(Recarga(1000,fechar,"Sambil"))
        billetera.consumir(consumo,PIN)
        self.assertEqual(billetera.PIN,PIN)
        self.assertGreaterEqual(billetera.balance, monto)
        self.assertLess(consumo.monto,0)

    def testConsumirNulo(self):
        monto=0
        fecha=datetime.date.today()
        establecimiento="Artorus"
        consumo=Consumo(monto,fecha,establecimiento)
        billetera=BilleteraElectronica(100,"Pepito","Perez",10000000,6969)
        PIN=6969
        fechar=datetime.date(2007,12,5)
        Recarga(1000,fechar,"Sambil")
        billetera.consumir(consumo,PIN)
        self.assertEqual(billetera.PIN,PIN)
        self.assertGreaterEqual(billetera.balance, monto)
        self.assertEqual(monto,0)
    
    def testConsumirPIN(self):
        monto=50
        fecha=datetime.date.today()
        establecimiento="Artorus"
        consumo=Consumo(monto,fecha,establecimiento)
        billetera=BilleteraElectronica(100,"Pepito","Perez",10000000,6969)
        PIN=6969
        fechar=date(2008,3,28)
        billetera.recargar(Recarga(1000,fechar,"Sambil"))
        billetera.consumir(consumo,PIN)
        self.assertEqual(billetera.PIN,PIN)
        self.assertGreaterEqual(billetera.balance, monto)
        self.assertGreater(monto,0)
    
    def testConsumirMayorBalance(self):
        monto=50
        fecha=date(2015,10,15)
        establecimiento="Artorus"
        consumo=Consumo(monto,fecha,establecimiento)
        billetera=BilleteraElectronica(100,"Pepito","Perez",10000000,6969)
        PIN=6969
        billetera.consumir(consumo,PIN)
        self.assertEqual(billetera.PIN,PIN)
        self.assertLessEqual(billetera.balance, monto)
        self.assertGreater(monto,0)

    def testConsumirIgualBalance(self):
        monto=1000
        fecha=datetime.date.today()
        establecimiento="Artorus"
        consumo=Consumo(monto,fecha,establecimiento)
        billetera=BilleteraElectronica(100,"Pepito","Perez",10000000,6969)
        PIN=6969
        fechar=date(2008,3,28)
        billetera.recargar(Recarga(1000,fechar,"Sambil"))
        billetera.consumir(consumo,PIN)
        self.assertEqual(billetera.PIN,PIN)
        self.assertGreaterEqual(billetera.balance, monto)
        self.assertGreater(monto,0)