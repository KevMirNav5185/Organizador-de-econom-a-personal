# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 22:39:56 2021

@author: Miranda Navarrete 1
"""

"""
El programa es un desglosador de ingresos mensuales en categorías de egresos.
E0 (Recibe ingreso mensual)
E1 (Entrega desglose del ingreso por categorías y un balance positivo, negativo o nulo)
"""
print("Te damos la bienvenida al sistema Tu Dinero Tu Bienestar (TDTB)\n")

balance=float(input("¿Cuánto dinero recibiste? -Ingreso mensual\n"))

print("Tu ingreso mensual es de: ", balance, " MXN \n")

costo_agua=float(input("¿Cuánto debes pagar por agua durante el mes? \n"))

balance = balance-costo_agua

costo_electricidad=float(input("¿Cuánto debes pagar por electricidad durante el mes? \n"))

balance = balance-costo_electricidad

costo_tel_cable=float(input("¿Cuánto debes pagar por teléfono y cable durante el mes? \n"))

balance = balance-costo_tel_cable

costo_gas=float(input("¿Cuánto debes pagar por gas durante el mes? \n"))

balance = balance-costo_gas

costo_transporte=float(input("¿Cuánto gastas en transporte (tarifa de camión o gasto en gasolina/servicio de transporte) durante el mes? \n"))

balance = balance-costo_transporte

costo_extra=float(input("¿Cuánto debes por algún gasto extra \n"))

balance = balance-costo_extra

print("Tu balance para este mes es de: ", balance, " MXN\n" )

print("Pagas por agua: ", costo_agua, " MXN\n")

print("Pagas por electricidad: ", costo_electricidad, " MXN\n")

print("Pagas por teléfono y cable: ", costo_tel_cable, " MXN\n")

print("Pagas por gas: ", costo_gas, " MXN\n")

print("Pagas por transporte: ", costo_transporte, " MXN\n")

print("Pagas por algún gasto extra: ", costo_extra, " MXN\n")


