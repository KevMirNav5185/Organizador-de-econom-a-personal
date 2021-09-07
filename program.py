"""
Organizador de economía personal.
El programa es un desglosador de ingresos mensuales en categorías de egresos.
Recibe un ingreso mensual y las cantidades de dinero que el usuario gasta 
por ciertas categorías. Al final entrega un balance y ya sea un desglose
completo por categoría de egreso, o solo las categorías de mayor
y menor gasto -en proceso-.
"""

"""-----------------------Comienza-Funciones--------------------------------"""

def egresos_totales(egresos,costo_agua,costo_electricidad, costo_telefono_cable,costo_gas,costo_transporte,costo_extra):
    """
    Recibe: estado inicial de egresos (egresos=0) y cantidades guardadas en cada categoría de costos.
    Se le suman todas las categorías de costo
    Devuelve: egresos totales
    """
    egresos=costo_agua
    egresos=egresos + costo_electricidad
    egresos=egresos + costo_telefono_cable
    egresos=egresos + costo_gas
    egresos=egresos + costo_transporte
    egresos=egresos + costo_extra
    return egresos

def calculo_balance(balance,egresos):
    """
    Recibe: ingreso mensual del usuario (balance) y estado inicial de 
    egresos (egresos=0)
    Se le resta al balance el total de egresos (egresos) calculado en la 
    funcion de egresos_totales
    Devuelve: balance reducido
    """
    return balance - egresos_totales(egresos,costo_agua,costo_electricidad, costo_telefono_cable,costo_gas,costo_transporte,costo_extra)

def egreso_maximo(costo_agua,costo_electricidad, costo_telefono_cable,costo_gas,costo_transporte,costo_extra):
  """
  Recibe: Cada categoría de egreso.
  Devuelve: Categoría con mayor valor
  """
  return max(costo_agua,costo_electricidad, costo_telefono_cable,costo_gas,costo_transporte,costo_extra)

def egreso_minimo(costo_agua,costo_electricidad, costo_telefono_cable,costo_gas,costo_transporte,costo_extra):
  """
  Recibe: Cada categoría de egreso.
  Devuelve: Categoría con menor valor
  """
  return min(costo_agua,costo_electricidad, costo_telefono_cable,costo_gas,costo_transporte,costo_extra)

"""----------------------Comienza-Código-Principal--------------------------"""
egresos=0

print("Te damos la bienvenida al sistema Tu Dinero Tu Bienestar (TDTB)")

balance = float(input("¿Cuánto dinero recibiste? -Ingreso mensual\n"))

print("\nTu ingreso mensual es de: ", balance, " MXN \n")

costo_agua = float(input("¿Cuánto debes pagar por agua durante el mes? \n"))

costo_electricidad = float(input("¿Cuánto debes pagar por electricidad durante\
 el mes? \n"))

costo_telefono_cable = float(input("¿Cuánto debes pagar por teléfono y cable\
 durante el mes? \n"))

costo_gas = float(input("¿Cuánto debes pagar por gas durante el mes? \n"))

costo_transporte = float(input("¿Cuánto gastas en transporte (tarifa de camión\
 o gasto en gasolina/servicio de transporte) durante el mes? \n"))

costo_extra = float(input("¿Cuánto debes por algún gasto extra \n"))

print("¿Qué necesitas?\n")
print("1. Desglose completo de egresos y balance final\n")
print("2. Categoría de egreso mayor y menor, con balance final\n")

opcion=int(input("Selecciona una función: "))
if opcion==1:
  print("\nTu balance para este mes es de: ", calculo_balance(balance,egresos), " MXN\n")
  print("Pagas por agua: ", costo_agua, " MXN\n")
  print("Pagas por electricidad: ", costo_electricidad, " MXN\n")
  print("Pagas por teléfono y cable: ", costo_telefono_cable, " MXN\n")
  print("Pagas por gas: ", costo_gas, " MXN\n")
  print("Pagas por transporte: ", costo_transporte, " MXN\n")
  print("Pagas por algún gasto extra: ", costo_extra, " MXN\n")
elif opcion==2:
  print("\nTu balance para este mes es de: ", calculo_balance(balance,egresos), " MXN\n")
  print("Mayor egreso: ", egreso_maximo(costo_agua,costo_electricidad,costo_telefono_cable,costo_gas,costo_transporte,costo_extra)," MXN por ")
  print("Menor ingreso", egreso_minimo(costo_agua,costo_electricidad, costo_telefono_cable,costo_gas,costo_transporte,costo_extra), " MXN por ")
else:
  print("Elija una opción válida")
