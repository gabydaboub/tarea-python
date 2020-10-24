class ingresos:
    def __init__(self):
        self.montoTotal = 0.0
        self.transaccionesIngresos = 0.0

    def agegarIngreso(self, ingreso):
        self.montoTotal = self.montoTotal + ingreso
        self.transaccionesIngresos =+ 1
        return self.montoTotal

    def getMontoTotal(self):
        total = self.montoTotal
        return total
    
    def getTransacciones(self):
        totalT = self.transaccionesIngresos
        return totalT

   