class CuentaBancaria:

    # atributos de clase
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []

    #constructor o inicializador
    def __init__(self, numero_cuenta, tasa_interes, balance):
        self.numero_cuenta = numero_cuenta
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

#!MÉTODOS DE OBJETO/INSTANCIA
    def re_tiro(self,cantidad):
        # podemos usar el método estático aquí para evaluar
        # si podemos retirar los fondos sin quedar con balance negativo
        if CuentaBancaria.puede_retirar(self.balance,cantidad):
            self.balance -= cantidad
        else:
            print("Fondos insuficientes")
        return self 

    # aumenta el balance de la cuenta segun la cantidad dada
    def deposito(self, cantidad):
        self.balance += cantidad
        return self

    #disminuye el balance de la cuenta en el monto dado si hay fondos suficientes; 
    # si no hay suficiente dinero, imprime el mensaje: 
    # "Fondos insuficientes: cobrando una tarifa de $5", y resta $5
    def retiro(self, cantidad):
        if self.balance < cantidad:
            self.balance -= 5
            print("Fondos Insuficientes, te restaremos 5")
        else:
            self.balance -= cantidad
        return self

    #imprime en la consola: por ejemplo, "Balance: $100"
    def mostrar_info_cuenta(self):
        print("Balance actual: ", self.balance)
        return self

    #aumenta el balance de la cuenta por el balance actual * la tasa de interés 
    # (siempre que el balance sea positivo) 
    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.tasa_interes)  
        return self

#!MÉTODOS DE CLASE
    # método de clase para cambiar el nombre del banco
    @classmethod
    def cambiar_nombre_banco(cls, name):
        cls.nombre_banco = name

    # método de clase para obtener balance de todas las cuentas
    @classmethod
    def todos_los_balances(cls):
        sum = 0
        # utilizamos cls para referirnos a la clase
        for account in cls.todas_las_cuentas:
            sum += balance.cuenta
        return sum

    @classmethod
    def imprimir_todas_cuentas(cls, parametro):
        for cuenta in cls.todas_las_cuentas:
            print(f"Esta cuenta tiene un balance de {cuenta.balance}")
            # print(cuenta.__dict__)

#!MÉTODOS DE ESTATICOS
    # los métodos estáticos no tienen acceso a ningún atributo
    # solo a lo que se le pasa
    @staticmethod
    def puede_retirar(balance,cantidad):
        if (balance - cantidad) < 0:
            return False
        else:
            return True
