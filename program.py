"""
Organizador de economía personal.
El programa es un desglosador de ingresos mensuales en categorías de egresos.
Recibe un ingreso mensual y las cantidades de dinero que el usuario gasta 
por ciertas categorías. Al final entrega un balance y ya sea un desglose
completo por categoría de egreso, o solo las categorías de mayor
y menor gasto junto con el balance.
"""

"""-----------------------Comienzan-Funciones--------------------------------"""


def egresos_totales(egresos, costo_agua, costo_electricidad, costo_telefono_cable, 
                    costo_gas, costo_transporte, costo_extra):
    """
    Recibe: estado inicial de egresos (egresos=0) y cantidades guardadas
    en cada categoría de costos.
    Se acumulan en egresos todas las categorías de costos
    Devuelve: egresos totales acumulados en la variable egresos
    """
    egresos = costo_agua
    egresos = egresos + costo_electricidad
    egresos = egresos + costo_telefono_cable
    egresos = egresos + costo_gas
    egresos = egresos + costo_transporte
    egresos = egresos + costo_extra
    return egresos


def calculo_balance(balance, egresos):
    """
    Recibe: ingreso mensual del usuario (balance) y los egresos acumulados
    Se le resta al balance el total de egresos
    Devuelve: balance reducido
    """
    balance = balance - egresos
    
    return balance


def identifica_categoria(valor_categoria, costo_agua, costo_electricidad,\
    costo_telefono_cable, costo_gas, costo_transporte, costo_extra):
   """
   Recibe: valor de la categoria a identificar y los valores de todas las
   categorias de egreso.
   Compara el valor de la categoría a identificar con cada uno de las 
   categorías de egreso.
   Devuelve: string que indica con cual categoría coincidió
   """    
   if valor_categoria == costo_agua:
    return " MXN por agua"
   elif valor_categoria == costo_electricidad:
    return " MXN por electricidad"
   elif valor_categoria == costo_telefono_cable:
    return " MXN por teléfono y cable"
   elif valor_categoria == costo_gas:
    return " MXN por gas"
   elif valor_categoria == costo_transporte:
    return " MXN por transporte"
   else:
    return "MXN por extra"


def tiempo_para_ahorro (dinero_acumulado, ahorro, balance,egresos,meta_ahorro,
                        porcentaje_ahorro, incremento_ingresos,
                        periodo_incremento_ingresos,incremento_egresos,
                        periodo_incremento_egresos,meses):
    
    """
    Recibe: una variable acumuladora (dinero acumulado), una variable
    ajustable para que el cálculo del ahorro se simplifique (ahorro),
    el balance, los egresos totales, una meta de ahorro, cuánto y 
    cada cuánto aumentaran los ingresos y egresos, y un contador
    que es lo que se requiere calcular (meses).
    La función calcula los meses necesarios para ahorrar cierta cantidad
    de dinero utilizando un ciclo while y dados ciertos parámetros
    (Explicación más detallada a un lado de los procesos)
    Regresa: Tiempo en meses.
    """
    
    while (dinero_acumulado<meta_ahorro): #Corre la operación mientras
                                          #no se cumpla la meta
    
        ahorro=calculo_balance(balance,egresos) #El balance del mes es la 
                                                #base del ahorro mensual
        ahorro=ahorro*porcentaje_ahorro #Se calcula el porcentaje ahorrado
                                        #del balance
        dinero_acumulado=dinero_acumulado + ahorro #Se va acumulando el ahorro
        
        meses=meses+1 #Se va avanzando en el tiempo mes por mes
        
        if meses==periodo_incremento_ingresos: #Haz el ajuste de ingresos
                                               #cuando se cumpla el periodo
            balance=balance + (balance*incremento_ingresos)
        if meses==periodo_incremento_egresos:  #Haz el ajuste de egresos cuando
                                               #se cumpla el periodo
            egresos=egresos + (egresos*incremento_egresos)
            
    return meses #Regresa el tiempo requerido


"""----------------------Comienza-Código-Principal--------------------------"""
print("Te damos la bienvenida al sistema Tu Dinero Tu Bienestar (TDTB)")

"""-------------Recopilación--de--datos---------------"""

balance = float(input("¿Cuánto dinero recibiste? -Ingreso mensual\n"))
#Comprobación
while balance<0:
        balance=float(input("Error. Ingrese un valor positivo: "))

print("\nTu ingreso mensual es de: ", balance, " MXN \n")

costo_agua = float(input("¿Cuánto debes pagar por agua durante el mes? \n"))
#Comprobación
while costo_agua<0:
    costo_agua=float(input("Error. Ingrese un valor positivo: "))

costo_electricidad = float(input("¿Cuánto debes pagar por electricidad durante\
 el mes? \n"))
#Comprobación
while costo_electricidad<0:
    costo_electricidad=float(input("Error. Ingrese un valor positivo: "))

costo_telefono_cable = float(input("¿Cuánto debes pagar por teléfono y cable\
 durante el mes? \n"))
#Comprobación
while costo_telefono_cable<0:
    costo_telefono_cable=float(input("Error. Ingrese un valor positivo: "))

costo_gas = float(input("¿Cuánto debes pagar por gas durante el mes? \n"))
#Comprobación
while costo_gas<0:
    costo_gas=float(input("Error. Ingrese un valor positivo: "))


costo_transporte = float(input("¿Cuánto gastas en transporte (tarifa de camión\
 o gasto en gasolina/servicio de transporte) durante el mes? \n"))
#Comprobación
while costo_transporte<0:
    costo_transporte=float(input("Error. Ingrese un valor positivo: "))

costo_extra = float(input("¿Cuánto debes por algún gasto extra \n"))
#Comprobación
while costo_extra<0:
    costo_extra=float(input("Error. Ingrese un valor positivo: "))

print("¿Qué necesitas?\n")
print("1. Desglose completo de egresos y balance final\n")
print("2. Categoría de egreso mayor y menor, con balance final\n")
print("3. Tiempo necesario para ahorrar una cantidad\n")


"""------------------Comienzan--menú--y--operaciones-----------------------"""
#Cálculo de los egresos totales
egresos=0
egresos=egresos_totales(egresos, costo_agua,costo_electricidad,
                        costo_telefono_cable,costo_gas, costo_transporte,
                        costo_extra)

opcion = int(input("Selecciona una función: "))

if opcion == 1:
  print("\nTu balance para este mes es de: ",
        calculo_balance(balance, egresos), " MXN\n")
  print("Pagas por agua: ", costo_agua, " MXN\n")
  print("Pagas por electricidad: ", costo_electricidad, " MXN\n")
  print("Pagas por teléfono y cable: ", costo_telefono_cable, " MXN\n")
  print("Pagas por gas: ", costo_gas, " MXN\n")
  print("Pagas por transporte: ", costo_transporte, " MXN\n")
  print("Pagas por algún gasto extra: ", costo_extra, " MXN\n")

elif opcion == 2:

  valor_maximo = max(costo_agua, costo_electricidad,\
  costo_telefono_cable, costo_gas, costo_transporte,costo_extra)
  valor_minimo = min(costo_agua, costo_electricidad,\
  costo_telefono_cable, costo_gas, costo_transporte, costo_extra)

  print("\nTu balance para este mes es de: ",
        calculo_balance(balance, egresos), " MXN\n")

  print("Egreso máximo: ", valor_maximo, identifica_categoria(valor_maximo,\
  costo_agua,costo_electricidad, costo_telefono_cable, costo_gas,\
  costo_transporte, costo_extra))

  print("Egreso minimo: ", valor_minimo, identifica_categoria(valor_minimo,\
  costo_agua,costo_electricidad, costo_telefono_cable, costo_gas,\
  costo_transporte, costo_extra))

elif opcion==3:
    meses=0 #contador
    ahorro=0.0 #variable de cambio que se ajusta
    dinero_acumulado=0.0  #acumulador
    
    """---------------Comienza recopilación de parámetros-------------------"""
    
    meta_ahorro= float(input("- Meta de ahorro (¿Cuánto se quiere ahorrar?): "))
    #Comprobación
    while meta_ahorro<0:
        meta_ahorro=float(input("Error. Ingrese un valor positivo: "))

    porcentaje_ahorro= float(input("- Porcentaje del balance a ahorrar mensualmente (Formato: 0.2=20%): "))
    #Comprobación
    while porcentaje_ahorro<0 or porcentaje_ahorro>1:
        porcentaje_ahorro=float(input("Error. Ingrese un valor decimal entre 0 y 1: "))
    
    print("\nAhora establece cuánto y cada cuántos meses aumentaran tus ingresos aproximadamente")
    incremento_ingresos= float(input("- Porcentaje de incremento de ingresos (Formato: 0.2=20%): "))
    #Comprobación
    while incremento_ingresos<0 or incremento_ingresos>1: 
        incremento_ingresos=float(input("Error. Ingrese un valor decimal entre 0 y 1: "))
    
    periodo_incremento_ingresos=int(input("- Periodo de incremento en meses: "))
    #Comprobación
    while periodo_incremento_ingresos<0:
        periodo_incremento_ingresos=int(input("Error. Ingrese un valor positivo: "))
    
    print("\nAhora establece cuánto y cada cuántos meses aumentaran tus egresos aproximadamente")
    incremento_egresos=float(input("- Porcentaje de incremento de egresos (Formato: 0.2=20%): "))
    #Comprobación
    while incremento_egresos<0 or incremento_egresos>1: 
        incremento_egresos=float(input("Error. Ingrese un valor decimal entre 0 y 1: "))
    
    periodo_incremento_egresos=int(input("- Periodo de incremento en meses: "))
    #Comprobación
    while periodo_incremento_egresos<0:
        periodo_incremento_egresos=int(input("Error. Ingrese un valor positivo: "))
    
    """--------------------Impresión de resultados-------------------------"""
    
    print("\nPara ahorrar ", meta_ahorro, " MXN bajo los siguientes parámetros: ")
    print("\nIngresos actuales: ", balance, " MXN")
    print("Egresos actuales: ", egresos, " MXN")
    print("Ahorrando el ", porcentaje_ahorro, " del balance")
    print("Los ingresos aumentan a razón de ",incremento_ingresos," cada ",\
    periodo_incremento_ingresos," mes/es")
    print("Los egresos aumentan a razón de ",incremento_egresos," cada ",\
    periodo_incremento_egresos," mes/es")
    print("\nSe requiere/n ", tiempo_para_ahorro (dinero_acumulado, ahorro,\
    balance,egresos, meta_ahorro, porcentaje_ahorro, incremento_ingresos,\
    periodo_incremento_ingresos, incremento_egresos,\
    periodo_incremento_egresos,meses), " mes/es")
    
else:
  print("Elija una opción válida")