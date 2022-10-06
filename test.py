from usuarios import Usuario
from cuentaBancaria import CuentaBancaria

usuario1 = Usuario("Carola", "muxeres@gmail.com", 1)
usuario1.cuenta.deposito(700).mostrar_info_cuenta()
usuario1.hacer_deposito(500).mostrar_balance_usuario()
usuario1.abrir_nueva_cuenta(2).mostrar_info_cuentas_usuario()

usuario2 = Usuario("Antonio", "centauro@mail.com", 90988768)
usuario2.hacer_deposito(500).hacer_retiro(100)
usuario2.abrir_nueva_cuenta(123432)
usuario2.hacer_deposito_en_cuenta(123432,100)
usuario2.mostrar_info_cuentas_usuario()

usuario3 = Usuario("casuza", "casuza@sega.com", 1220)
usuario3.mostrar_info_cuentas_usuario()
usuario3.hacer_deposito_en_cuenta(1220,500)
usuario3.mostrar_info_cuentas_usuario()
