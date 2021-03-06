"""
Autor: Kevin Alejandro Miranda Navarrete
Matrícula: A01705185
Título del proyecto: Organizador de economía personal
El programa cuenta con 4 diferentes funciones relevantes para el manejo de
la economía personal:
1. Desglose completo de egresos y balance final
2. Muestra la categoría de egreso mayor y menor, con balance final
3. Tiempo necesario para ahorrar una cantidad y gráfica del ahorro a través del
    tiempo.
4. Cálculo de la ganancia, gasto y margen promedio diarios o semanales.
Recibe principalmente un ingreso mensual y las cantidades de dinero que el
usuario gasta por ciertas categorías. Dependiendo de la función, recibe otros
valores. Al final, ejecuta la función que desee el usuario.
"""

import pygal  # Importa libreria "pygal" para generar gráficas
"""
La librería pygal permite crear gráficas de todo tipo, así como visualizarlas
en diversos formatos o en un navegador. La escogí porque era sencilla de utilizar
y flexible en cuanto a poder visualizar los gráficos en navegador, permitiendo
que el código funcione en casi cualquier equipo. La guía de su uso que utilicé es
esta: http://www.pygal.org/en/stable/documentation/first_steps.html

Líneas de código donde se ve su uso:
    307 a 322 Generación de gráfica en función principal 3
"""


"""-----------------------Comienzan-Funciones--------------------------------"""


def egresos_totales(egresos, lista_egresos):
  """
  Recibe: Variable "egresos" que albergará el acumulado de la suma de todos 
  los egresos y lista con los valores de los egresos.
  Recorre cada elemento de la lista y lo acumúla dentro de la variable de "egresos".
  Devuelve: variable "egresos" 
  """
  for i in lista_egresos:
    egresos = egresos+i
  return egresos


def calculo_balance(balance, ingreso, egresos):
    """
    Recibe: Estado inicial del balance (balance=0),ingreso mensual del
    usuario (ingreso) y los egresos acumulados en
    "egresos".
    Se le resta al ingreso el total de egresos y se guarda en balance.
    Devuelve: balance.
    """
    balance = ingreso - egresos

    return balance


def identifica_categoria(valor_categoria, lista_egresos):
  """
  Recibe: Valor de la categoría a identificar y la lista de egresos con los
  valores.
  Compara el valor de la categoría con el valor de cada localidad.
  Devuelve: string que indica con cual categoría coincidió
  """
  if valor_categoria == lista_egresos[0]:
    return " MXN por alimento"
  elif valor_categoria == lista_egresos[1]:
    return " MXN por despensa"
  elif valor_categoria == lista_egresos[2]:
    return " MXN por agua"
  elif valor_categoria == lista_egresos[3]:
    return " MXN por electricidad"
  elif valor_categoria == lista_egresos[4]:
    return " MXN por teléfono y cable"
  elif valor_categoria == lista_egresos[5]:
    return " MXN por gas"
  elif valor_categoria == lista_egresos[6]:
    return " MXN por transporte"
  else:
    return " MXN por algún gasto extra"


def tiempo_para_ahorro(dinero_acumulado, lista_dinero_acumulado, ahorro,
                       balance, ingreso, egresos, meta_ahorro,
                       porcentaje_ahorro, incremento_ingresos,
                       periodo_incremento_ingresos, incremento_egresos,
                       periodo_incremento_egresos, meses, lista_meses):
    """
    Recibe: una variable acumuladora (dinero acumulado), una lista para guardar
    sus distintos valores a través del tiempo (lista_dinero_acumulado), una 
    variable ajustable para que el cálculo del ahorro se simplifique (ahorro),
    el balance, el ingreso mensual, los egresos totales, una meta de ahorro, cuánto y 
    cada cuánto aumentaran los ingresos y egresos, un contador
    que es lo que se requiere calcular (meses) y una lista para guardar
    sus distintos valores a través del tiempo (lista_meses).
    La función calcula los meses necesarios para ahorrar cierta cantidad
    de dinero utilizando un ciclo while y dados ciertos parámetros. Además de
    que guarda los valores del dinero acumulado y los meses en una lista para graficar.
    (Explicación más detallada a un lado de los procesos)
    Regresa: Tiempo en meses.
    """

    while (dinero_acumulado < meta_ahorro): # Corre la operación mientras no se cumpla la meta

        # El balance del mes es la base del ahorro mensual
        ahorro = calculo_balance(balance, ingreso, egresos)
        
        if ahorro > 0: # Se calcula el porcentaje ahorrado solo si hay un balance positivo
          ahorro = ahorro*porcentaje_ahorro
          
        dinero_acumulado = dinero_acumulado + ahorro  # Se va acumulando el ahorro

        lista_dinero_acumulado.append(dinero_acumulado) # Agrega el ahorro a una lista para graficar

        meses = meses+1  # Se va avanzando en el tiempo mes por mes

        lista_meses.append(meses)  # Agrega el mes a una la lista para graficar

        if (meses % periodo_incremento_ingresos) == 0:  # Haz el ajuste de ingresos cuando se cumpla el periodo
            ingreso = ingreso + (ingreso*incremento_ingresos)
        if (meses % periodo_incremento_egresos) == 0:  # Haz el ajuste de egresos cuando se cumpla el periodo
            egresos = egresos + (egresos*incremento_egresos)

    return meses  # Regresa el tiempo requerido


def calculo_valor_en_periodo(valor, periodo):
  """
  Recibe: valor a calcular (ingreso o egreso) y el código del periodo de tiempo.
  Identifica si se seleccionó diario o semanal: Si fue diario (1), se divide el
  valor entre el promedio de días en un mes del año. Si fue semanal (2),
  se divide el valor entre el número de semanas en un mes. 
  Se guarda el valor en una auxiliar (reporte).
  Devuelve: auxiliar (reporte)
  """
  if periodo == 1:  # 1, diario
    reporte = valor/30.417  # valor/promedio de días en un mes del año
  elif periodo == 2:  # 2, semanal
    reporte = valor/4  # valor/semanas en un mes
  return ("%.2f" % (reporte))


"""----------------------Comienza-Código-Principal--------------------------"""
print("Te damos la bienvenida al sistema Tu Dinero Tu Bienestar (TDTB)")

"""------------------Recopilación--de--datos---------------------------------"""

ingreso = float(input("¿Cuánto dinero recibiste? -Ingreso mensual\n"))
#Comprobación
while ingreso < 0:
    ingreso = float(input("Error. Ingrese un valor positivo: "))

print("\nTu ingreso mensual es de: ", ingreso, " MXN \n")

#Lista con las indicaciones para el usuario
lista_egresos = ["¿Cuánto debes pagar por alimento durante el mes? ",
                 "¿Cuánto debes pagar por despensa durante el mes? ",
                 "¿Cuánto debes pagar por agua durante el mes? ",
                 "¿Cuánto debes pagar por electricidad durante el mes? ",
                 "¿Cuánto debes pagar por teléfono y cable durante el mes? ",
                 "¿Cuánto debes pagar por gas durante el mes? ",
                 "¿Cuánto gastas en transporte (tarifa de camión o gasto en gasolina/servicio de transporte) durante el mes? ",
                 "¿Cuánto debes por algún gasto extra "]

""" Descripción de la lista:
    [Alimento] 0, [Despensa] 1, [Agua] 2, [Electricidad] 3, [Tel y cable] 4,
    [Gas] 5, [Transporte] 6, [Extra] 7 """

"""Función: Registra cada categoría de egresos al reemplazar cada elemento de
la lista por un float """
j = 0  # Contador

for i in lista_egresos:
  print(i)  # Muestra indicación
  egreso_agregado = float(input())  # Valor a agregar

  #Comprobación
  while egreso_agregado < 0:
    egreso_agregado = float(input("Error. Ingrese un valor positivo: "))

  # Sustituye el string por el float ingresado
  lista_egresos[j] = egreso_agregado
  j = j+1  # Avanza de localidad

"""------------------Comienzan--menú--y--operaciones-----------------------"""

print("¿Qué necesitas?\n")
print("1. Desglose completo de egresos y balance final")
print("2. Categoría de egreso mayor y menor, con balance final")
print("3. Tiempo necesario para ahorrar una cantidad y gráfica del ahorro a través del tiempo")
print("4. Ganancia, gasto y margen promedio diarios o semanales")

#Cálculo de los egresos totales
egresos = 0
egresos = egresos_totales(egresos, lista_egresos)

#Cálculo del balance
balance = 0
balance = calculo_balance(balance, ingreso, egresos)

opcion = int(input("Selecciona una función: "))
#Comprobación
while (opcion!=1) and (opcion!=2) and (opcion!=3) and (opcion!=4):
    opcion = int(input("Error. Selecciona un número entre 1 y 4: "))

if opcion == 1:
  print("\nTu balance para este mes es de: ",
        balance, " MXN\n")

  """Desglose por categorías:
     Imprime el valor en la posición relacionada al orden ya establecido"""
     
  print("Pagas por alimento: ", lista_egresos[0], " MXN\n")
  print("Pagas por despensa: ", lista_egresos[1], " MXN\n")
  print("Pagas por agua: ", lista_egresos[2], " MXN\n")
  print("Pagas por electricidad: ", lista_egresos[3], " MXN\n")
  print("Pagas por teléfono y cable: ", lista_egresos[4], " MXN\n")
  print("Pagas por gas: ", lista_egresos[5], " MXN\n")
  print("Pagas por transporte: ", lista_egresos[6], " MXN\n")
  print("Pagas por algún gasto extra: ", lista_egresos[7], " MXN\n")

elif opcion == 2:

  valor_maximo = max(lista_egresos)
  valor_minimo = min(lista_egresos)

  print("\nTu balance para este mes es de: ",
        balance, " MXN\n")

  print("Egreso maximo: ", valor_maximo,
        identifica_categoria(valor_maximo, lista_egresos))

  print("Egreso minimo: ", valor_minimo,
        identifica_categoria(valor_minimo, lista_egresos))

elif opcion == 3:
    meses = 0  # contador
    ahorro = 0.0  # variable de cambio que se ajusta
    dinero_acumulado = 0.0  # acumulador
    lista_dinero_acumulado = [0] # lista con el rango de la gráfica ahorro vs tiempo
    lista_meses = [0]  # lista con el dominio de la gráfica ahorro vs tiempo

    """---------------Comienza recopilación de parámetros-------------------"""

    meta_ahorro = float(
        input("- Meta de ahorro (¿Cuánto se quiere ahorrar?): "))
    #Comprobación
    while meta_ahorro < 0:
        meta_ahorro = float(input("Error. Ingrese un valor positivo: "))

    porcentaje_ahorro = float(
        input("- Porcentaje del balance a ahorrar mensualmente (Formato: 0.2=20%): "))
    #Comprobación
    while porcentaje_ahorro < 0 or porcentaje_ahorro > 1:
        porcentaje_ahorro = float(
            input("Error. Ingrese un valor decimal entre 0 y 1: "))

    print("\nAhora establece cuánto y cada cuántos meses aumentaran tus ingresos aproximadamente")
    incremento_ingresos = float(
        input("- Porcentaje de incremento de ingresos (Formato: 0.2=20%): "))
    #Comprobación
    while incremento_ingresos < 0 or incremento_ingresos > 1:
        incremento_ingresos = float(
            input("Error. Ingrese un valor decimal entre 0 y 1: "))

    periodo_incremento_ingresos = int(
        input("- Periodo de incremento en meses: "))
    #Comprobación
    while periodo_incremento_ingresos < 0:
        periodo_incremento_ingresos = int(
            input("Error. Ingrese un valor positivo: "))

    print("\nAhora establece cuánto y cada cuántos meses aumentaran tus egresos aproximadamente")
    incremento_egresos = float(
        input("- Porcentaje de incremento de egresos (Formato: 0.2=20%): "))
    #Comprobación
    while incremento_egresos < 0 or incremento_egresos > 1:
        incremento_egresos = float(
            input("Error. Ingrese un valor decimal entre 0 y 1: "))

    periodo_incremento_egresos = int(
        input("- Periodo de incremento en meses: "))
    #Comprobación
    while periodo_incremento_egresos < 0:
        periodo_incremento_egresos = int(
            input("Error. Ingrese un valor positivo: "))

    """--------------------Impresión de resultados-------------------------"""

    print("\nPara ahorrar ", meta_ahorro,
          " MXN bajo los siguientes parámetros: ")
    print("\nIngresos actuales: ", ingreso, " MXN")
    print("Egresos actuales: ", egresos, " MXN")
    print("Ahorrando el ", porcentaje_ahorro, " del balance")
    print("Los ingresos aumentan a razón de ", incremento_ingresos, " cada ",
          periodo_incremento_ingresos, " mes/es")
    print("Los egresos aumentan a razón de ", incremento_egresos, " cada ",
          periodo_incremento_egresos, " mes/es")
    print("\nSe requiere/n ", tiempo_para_ahorro(dinero_acumulado, lista_dinero_acumulado,
                                                 ahorro, balance, ingreso,
                                                 egresos, meta_ahorro,
                                                 porcentaje_ahorro,
                                                 incremento_ingresos,
                                                 periodo_incremento_ingresos,
                                                 incremento_egresos,
                                                 periodo_incremento_egresos,
                                                 meses, lista_meses),
          " mes/es")

    """--------------------Generación de gráfica---------------------------
    
    Genera una gráfica lineal con título "Ahorro a través de los meses" y
    títulos del dominio "Mes" y rango "Ahorro (MXN)"           """
    
    grafica_ahorro_tiempo = pygal.Line(title='Ahorro a través de los meses',
                                       x_title='Mes', y_title='MXN')

    #Establece la lista_meses como los valores del dominio tipo integers
    grafica_ahorro_tiempo.x_labels = map(int, lista_meses)

    #Agrega los valores de la lista_dinero_acumulado con una leyenda
    grafica_ahorro_tiempo.add("Ahorro (MXN)", lista_dinero_acumulado)

    #Abre la gráfica dentro de un navegador
    grafica_ahorro_tiempo.render_in_browser()


elif opcion == 4:
  print("\nEstablece el periodo de tiempo para el cálculo")
  print("1. Reporte diario")
  print("2. Reporte semanal")
  periodo = int(input("Selecciona un periodo de tiempo: "))

  #Comprobación
  while (periodo != 1) and (periodo != 2):
    periodo = int(input("Error. Selecciona 1 o 2: "))

  if periodo == 1:
    print("\nIngreso diario promedio: ",
          calculo_valor_en_periodo(ingreso, periodo), " MXN")
    print("Egreso diario promedio: ",
          calculo_valor_en_periodo(egresos, periodo), " MXN")
    print("Margen diario promedio: ",
          calculo_valor_en_periodo(balance, periodo), " MXN")
  else:
    print("\nIngreso semanal promedio: ",
          calculo_valor_en_periodo(ingreso, periodo), " MXN")
    print("Egreso semanal promedio: ",
          calculo_valor_en_periodo(egresos, periodo), " MXN")
    print("Margen diario promedio: ",
          calculo_valor_en_periodo(balance, periodo), " MXN")