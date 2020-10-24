class egresos:
    def __init__(self):
        self.montoTotal = 0
        self.transaccionesEgresos = 0

    def agregarEgreso(self, egreso):
        self.montoTotal = self.montoTotal + egreso
        self.transaccionesEgresos += 1
        return self.montoTotal

    def getMontoTotal(self):
        total = self.montoTotal
        return total
    
    def getTransacciones(self):
        totalT = self.transaccionesEgresos
        return totalT

   