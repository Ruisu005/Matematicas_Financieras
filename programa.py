from datetime import datetime, timedelta
from math import floor
import math

def calcular_capital(monto, tasa, plazo):
    plazo = plazo/12
    tasa = tasa/100
    capital = monto / (1 + tasa * plazo)
    #capital = monto / ((1 + tasa / 100) ** plazo)
    return capital

def calcular_monto(capital, tasa, plazo):
    plazo = plazo/12
    tasa = tasa/100
    monto = capital * (1 + tasa * plazo)
    return monto

def calcular_tasa(capital, monto, plazo):
    plazo = plazo/12
    # tasa = tasa/100
    tasa = (monto / capital -1) / plazo
    tasa = tasa *100
    return tasa

def calcular_plazo(monto, capital, tasa):
    tasa = tasa/100
    plazo = ((monto / capital) - 1) / tasa
    return plazo

def convertir_a_anios_meses_dias(plazo_anios):
    anios = int(plazo_anios)
    meses_flotante = (plazo_anios - anios) * 12
    meses = int(meses_flotante)
    dias_flotante = (meses_flotante - meses) * (365.25 / 12)  # Considerando el año como 365.25 días
    dias = round(dias_flotante)
    return anios, meses, dias

def calcular_descuento_y_precio_final(plazo, porcentaje_descuento, precio_original):
    descuento = precio_original * (plazo / 12) * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    return descuento, precio_final

def calcular_valor_comercial(valor_original, dias_totales, interes, descuento):
    monto = valor_original * (1 + (dias_totales / 365) * (interes / 100))
    valor_comercial = monto * (1 - (dias_totales / 365) * (descuento / 100))
    return valor_comercial

def calcular_fecha_negociacion(valor_inicial, valor_final, descuento):
    fecha_negociacion = (1 - (valor_inicial / valor_final)) / (descuento / 100)
    fecha_negociacion *= 365  # Convertir a días (asumiendo un año de 365 días)
    return floor(fecha_negociacion)  # Redondear hacia abajo los días transcurridos

def calcular_fecha_a_partir_dias_transcurridos(fecha_inicio, dias_transcurridos):
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")

    fecha_calculada = fecha_inicio + timedelta(days=dias_transcurridos)
    return fecha_calculada.strftime('%Y-%m-%d')

def calcular_tasa_interes_anual(credito, valor_final, dias_inicio_final):
    tasa_interes = ((valor_final / credito) - 1) / (dias_inicio_final / 365)
    return tasa_interes

def calcular_dias_transcurridos(fecha_inicio, fecha_fin):
    fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin_dt = datetime.strptime(fecha_fin, "%Y-%m-%d")
    dias_transcurridos = (fecha_fin_dt - fecha_inicio_dt).days
    return dias_transcurridos

def calcular_monto(credito, tasa_interes, dias_transcurridos):
    monto = credito * (1 + (tasa_interes / 100) * (dias_transcurridos / 365))
    return monto

def calcular_precio_compra_venta(monto_calculado, dias_inicio_final, descuento):
    precio_compra_venta = monto_calculado * (1 - (dias_inicio_final / 365) * (descuento/100))
    return precio_compra_venta

def calcular_monto_compuesto(capital, interes, plazo, periodo_capitalizacion):
    tasa_capitalizable = (interes / 100) / periodo_capitalizacion
    numero_periodos = plazo * periodo_capitalizacion
    monto_compuesto = capital * (1 + tasa_capitalizable) ** numero_periodos
    return monto_compuesto

def calcular_capital_compuesto(monto, interes, plazo, periodo_capitalizacion):
    tasa_capitalizable = (interes / 100) / periodo_capitalizacion
    numero_periodos = (plazo/12) * periodo_capitalizacion
    capital_compuesto = monto / (1 + tasa_capitalizable) ** numero_periodos
    return capital_compuesto

def calcular_interes_compuesto(monto, capital, plazo, periodo_capitalizacion):
    numero_periodos = plazo * periodo_capitalizacion
    interes_compuesto = (monto / capital) ** (1 / numero_periodos) - 1
    interes_compuesto *= periodo_capitalizacion
    return interes_compuesto

def calcular_numero_periodos_compuesto(monto, capital, interes, periodo_capitalizacion):
    tasa_interes = interes / 100
    numero_periodos_compuesto = math.log(monto / capital) / math.log(1 + tasa_interes / periodo_capitalizacion)
    return numero_periodos_compuesto

def calcular_tasa_interes_desconocida(tasa_interes, periodo_capitalizacion_conocida, periodo_capitalizacion):
    tasa_interes_conocida = tasa_interes / 100
    tasa_interes_desconocida = math.sqrt((1 + tasa_interes_conocida / periodo_capitalizacion) ** periodo_capitalizacion) - 1
    tasa_interes_desconocida *= periodo_capitalizacion_conocida
    return tasa_interes_desconocida

def calcular_tasa_efectiva(tasa_efectiva_equivalente, periodo_capitalizacion):
    tasa_efectiva_equivalente = tasa_efectiva_equivalente / 100
    tasa_efectiva = ((1 + tasa_efectiva_equivalente / periodo_capitalizacion) ** periodo_capitalizacion) - 1
    return tasa_efectiva

def calcular_numero_de_rentas(monto, renta, tasa_capitalizable, periodo_capitalizacion):
    tasa_capitalizable = (tasa_capitalizable / 100) / periodo_capitalizacion
    numero_de_rentas = math.log(((monto / renta) * tasa_capitalizable) / (1 + tasa_capitalizable) + 1) / math.log(1 + tasa_capitalizable)
    return math.ceil(numero_de_rentas)

# Función para calcular rentaNueva
def calcular_renta_nueva(monto, tasa_capitalizable, numero_rentas_calculado):
    tasa_capitalizable = (tasa_capitalizable / 100)
    rentaNueva = (monto * tasa_capitalizable) / (1 + tasa_capitalizable) * (1 + tasa_capitalizable ** numero_rentas_calculado) - 1
    return rentaNueva

# Función para calcular nuevoMonto
def calcular_nuevo_monto(renta_nueva_calculada, tasa_capitalizable, numero_rentas_calculado):
    tasa_capitalizable = (tasa_capitalizable / 100)
    nuevoMonto = renta_nueva_calculada * (1 + tasa_capitalizable) * (1 + tasa_capitalizable ** numero_rentas_calculado) - 1 / tasa_capitalizable
    return nuevoMonto

def calcular_anualidad_vencida(capital, renta, tasa_capitalizable, periodo_capitalizacion):
    tasa_capitalizable = (tasa_capitalizable / 100) / periodo_capitalizacion
    anualidad_vencida = -math.log(1 - (capital / renta) * tasa_capitalizable) / math.log(1 + tasa_capitalizable)
    return math.ceil(anualidad_vencida)

def calcular_nueva_renta(capital, tasa_capitalizable, anualidad_vencida_calculada):
    nueva_renta = capital / ((1 - (1 + tasa_capitalizable) ** -anualidad_vencida_calculada) / anualidad_vencida_calculada)
    return nueva_renta

def calcular_amortizacion(monto_prestamo, tasa_interes_anual, numero_pagos):
    tasa_interes_mensual = tasa_interes_anual / 12 / 100
    cuota = monto_prestamo * (tasa_interes_mensual / (1 - (1 + tasa_interes_mensual) ** -numero_pagos))
    saldo_pendiente = monto_prestamo
    
    tabla_amortizacion = []
    for i in range(1, numero_pagos + 1):
        interes = saldo_pendiente * tasa_interes_mensual
        amortizacion = cuota - interes
        saldo_pendiente -= amortizacion
        
        tabla_amortizacion.append([i, round(cuota, 2), round(amortizacion, 2), round(interes, 2), round(saldo_pendiente, 2)])
    
    return tabla_amortizacion

# Menu
opcion = int(input("Selecciona una opción: \n"
                   "1. Calcular Capital\n"
                   "2. Calcular Monto\n"
                   "3. Calcular Tasa\n"
                   "4. Calcular Plazo\n"
                   "5. Calcular Descuento Simple\n"
                   "6. Calcular Valor Comercial\n"
                   "7. Calcular que Dia se Negocia un Documento\n"
                   "8. Calcular el Precio de Compra-Venta\n"
                   "9. Calcular Monto Compusto\n"
                   "10. Calcular Capital Compuesto\n"
                   "11. Calcular Interes Compuesto\n"
                   "12. Calcular Numero de Periodos Compuesto\n"
                   "13. Calcular Tasa de Interes Desconocida\n"
                   "14. Calcular Tasa Efectiva\n"
                   "15. Calcular Numero de Rentas\n"
                   "16. Calcular Anualidad Vencida\n"
                   "17. Calcular Amortizacion\n"
                   "Opcion: "))
capital = float
if opcion == 1:
    monto = float(input("Ingresa el monto: "))
    tasa = float(input("Ingresa la tasa de interés (en porcentaje): "))
    plazo = float(input("Ingresa el plazo (en años): "))
    capital = calcular_capital(monto, tasa, plazo)
    print(f"El capital es: {capital}")
elif opcion == 2:
    capital = float(input("Ingresa el capital: "))
    tasa = float(input("Ingresa la tasa de interés (en porcentaje): "))
    plazo = float(input("Ingresa el plazo (en años): "))
    monto = calcular_monto(capital, tasa, plazo)
    print(f"El monto es: {monto}")
elif opcion == 3:
    capital = float(input("Ingresa el capital: "))
    monto = float(input("Ingresa el monto: "))
    plazo = float(input("Ingresa el plazo (en años): "))
    tasa = calcular_tasa(capital, monto, plazo)
    print(f"La tasa de interés es: {tasa}%")
elif opcion == 4:
    capital = float(input("Ingresa el capital: "))
    monto = float(input("Ingresa el monto: "))
    tasa = float(input("Ingresa la tasa de interés (en porcentaje): "))
    plazo = calcular_plazo(capital, monto, tasa)
    print(f"El plazo es: {plazo} años")
elif opcion == 5:
    precio_original = float(input("Ingrese el precio original del producto: "))
    plazo = float(input("Ingrese el plazo en meses: "))
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
    descuento_calculado, precio_final_calculado = calcular_descuento_y_precio_final(plazo, porcentaje_descuento, precio_original)
    print(f"El descuento es: {descuento_calculado}")
    print(f"El precio final después del descuento es: {precio_final_calculado}")
elif opcion == 6:
    # Obtener la cantidad de pagos y sumar los días ingresados
    cantidad_pagos = float(input("Ingrese la cantidad de pagos a realizar: "))
    dias_totales = sum([float(input(f"Ingrese los días del pago {i + 1}: ")) for i in range(cantidad_pagos)])
    valor_original = float(input("Ingrese el valor original del producto: "))
    interes = float(input("Ingrese el porcentaje de interés: "))
    descuento = float(input("Ingrese el porcentaje de descuento: "))
    valor_comercial_calculado = calcular_valor_comercial(valor_original, dias_totales, interes, descuento)
    print(f"El valor comercial después de los días y descuentos es: {valor_comercial_calculado}")
elif opcion == 7:
    valor_inicial = float(input("Ingrese el valor inicial: "))
    valor_final = float(input("Ingrese el valor final: "))
    descuento = float(input("Ingrese el porcentaje de descuento: "))
    credito = float(input("Ingrese el credito de la mercancia: "))
    # Calcular los días transcurridos
    dias_transcurridos = calcular_fecha_negociacion(valor_inicial, valor_final, descuento)
    # Obtener la fecha de inicio
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
    # Calcular los días transcurridos entre la fecha de inicio y fin
    fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin_dt = datetime.strptime(fecha_fin, "%Y-%m-%d")
    dias_inicio_final = (fecha_fin_dt - fecha_inicio_dt).days
    # Calcular la fecha resultante a partir de los días transcurridos
    fecha_resultante = calcular_fecha_a_partir_dias_transcurridos(fecha_inicio, dias_transcurridos)
    # Calcular la tasa de interés anual
    tasa_interes_calculada = calcular_tasa_interes_anual(valor_inicial, valor_final, dias_inicio_final)
    print(f"La fecha de negociación estimada es aproximadamente en {dias_transcurridos} días.")
    print(f"La fecha correspondiente a esos días transcurridos es: {fecha_resultante}")
    print(f"La cantidad de días desde el inicio hasta la fecha final es: {dias_inicio_final}")
    print(f"La tasa de interés anual calculada es: {tasa_interes_calculada * 100:.2f}%")
elif opcion == 8:
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
    # Calcular los días transcurridos entre las fechas proporcionadas
    dias_transcurridos = calcular_dias_transcurridos(fecha_inicio, fecha_fin)
    # Obtener los valores necesarios para calcular el monto
    credito = float(input("Ingrese el monto del crédito: "))
    tasa_interes = float(input("Ingrese la tasa de interés: "))
    # Calcular el monto utilizando la fórmula proporcionada
    monto_calculado = calcular_monto(credito, tasa_interes, dias_transcurridos)
    # Obtener el descuento y los días desde inicio hasta fin
    descuento = float(input("Ingrese el descuento: "))
    dias_inicio_final = float(input("Ingrese la cantidad de días desde que ampara hasta la fecha final: "))
    # Calcular el precio de compra-venta utilizando la fórmula proporcionada
    precio_compra_venta = calcular_precio_compra_venta(monto_calculado, dias_inicio_final, descuento)
    print(f"Los días transcurridos entre {fecha_inicio} y {fecha_fin} son: {dias_transcurridos}")
    print(f"El monto calculado es: {monto_calculado}")
    print(f"El precio de compra-venta es: {precio_compra_venta}")
elif opcion == 9:
    capital = float(input("Ingrese el capital inicial: "))
    interes = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
    plazo = float(input("Ingrese el plazo en años: "))
    periodo_capitalizacion = int(input("Ingrese el período de capitalización (en años): "))
    # Calcular el monto compuesto utilizando la fórmula proporcionada
    monto_calculado = calcular_monto_compuesto(capital, interes, plazo, periodo_capitalizacion)
    print(f"El monto compuesto al final del período es: {monto_calculado}")
elif opcion == 10:
    monto = float(input("Ingrese el monto al final del período: "))
    interes = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
    plazo = float(input("Ingrese el plazo: "))
    periodo_capitalizacion = int(input("Ingrese el período de capitalización: "))
    # Calcular el capital compuesto utilizando la fórmula proporcionada
    capital_calculado = calcular_capital_compuesto(monto, interes, plazo, periodo_capitalizacion)
    print(f"El capital inicial necesario es: {capital_calculado}")
elif opcion == 11:
    monto = float(input("Ingrese el monto al final del período: "))
    capital = float(input("Ingrese el capital inicial: "))
    plazo = float(input("Ingrese el plazo: "))
    periodo_capitalizacion = int(input("Ingrese el período de capitalización: "))
    # Calcular el interés compuesto utilizando la fórmula ajustada
    interes_calculado = calcular_interes_compuesto(monto, capital, plazo, periodo_capitalizacion)
    # Mostrar el resultado normal
    print(f"El interés compuesto es: {interes_calculado}")
    # Mostrar el resultado convertido a porcentaje
    interes_porcentaje = interes_calculado * 100
    print(f"El interés compuesto en porcentaje es: {interes_porcentaje:.2f}%")
elif opcion == 12:
    monto = float(input("Ingrese el monto al final del período: "))
    capital = float(input("Ingrese el capital inicial: "))
    interes = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
    periodo_capitalizacion = float(input("Ingrese el período de capitalización (en años): "))
    dias_transcurrir = float(input("Ingrese la cantidad de días a transcurrir: "))
    # Calcular el número de periodos para el interés compuesto
    numero_periodos = calcular_numero_periodos_compuesto(monto, capital, interes, periodo_capitalizacion)
    # Multiplicar el resultado por la cantidad de días a transcurrir y redondearlo
    resultado_final = round(numero_periodos * dias_transcurrir)
    print(f"El número de días es: {resultado_final}")
elif opcion == 13:
    tasa_interes = float(input("Ingrese la tasa de interés conocida anual: "))
    periodo_capitalizacion_conocida = float(input("Ingrese el periodo de capitalización conocido: "))
    periodo_capitalizacion = float(input("Ingrese el periodo de capitalización desconocida: "))
    # Calcular la tasa de interés desconocida utilizando la fórmula proporcionada
    tasa_interes_desconocida = calcular_tasa_interes_desconocida(tasa_interes, periodo_capitalizacion_conocida, periodo_capitalizacion)
    # Mostrar el resultado como tasa de interés en porcentaje
    tasa_interes_desconocida_porcentaje = tasa_interes_desconocida * 100
    print(f"La tasa de interés desconocida es: {tasa_interes_desconocida} o {tasa_interes_desconocida_porcentaje:.2f}%")
elif opcion == 14:
    tasa_efectiva_equivalente = float(input("Ingrese la tasa efectiva equivalente (en porcentaje): "))
    periodo_capitalizacion = int(input("Ingrese el período de capitalización (en años): "))
    # Calcular la tasa efectiva utilizando la fórmula proporcionada
    tasa_efectiva_calculada = calcular_tasa_efectiva(tasa_efectiva_equivalente, periodo_capitalizacion)
    # Mostrar el resultado como tasa de interés en porcentaje
    tasa_efectiva_calculada_porcentaje = tasa_efectiva_calculada * 100
    print(f"La tasa efectiva resultante es: {tasa_efectiva_calculada} o {tasa_efectiva_calculada_porcentaje:.2f}%")
elif opcion == 15:
    monto = float(input("Ingrese el monto: "))
    renta = float(input("Ingrese la renta: "))
    tasa_capitalizable = float(input("Ingrese la tasa capitalizable (en porcentaje): "))
    periodo_capitalizacion = int(input("Ingrese el periodo de capitalización: "))
    # Calcular el número de rentas utilizando la fórmula proporcionada y redondearlo hacia arriba
    numero_rentas_calculado = calcular_numero_de_rentas(monto, renta, tasa_capitalizable, periodo_capitalizacion)
    # Calcular rentaNueva utilizando la fórmula proporcionada
    renta_nueva_calculada = calcular_renta_nueva(monto, tasa_capitalizable, numero_rentas_calculado)
    # Calcular nuevoMonto utilizando la fórmula proporcionada
    nuevo_monto_calculado = calcular_nuevo_monto(renta_nueva_calculada, tasa_capitalizable, numero_rentas_calculado)
    print(f"El número de rentas es: {numero_rentas_calculado}")
    print(f"La renta nueva es: {renta_nueva_calculada}")
    print(f"El nuevo monto es: {nuevo_monto_calculado}")
elif opcion == 16:
    capital = float(input("Ingrese el capital: "))
    renta = float(input("Ingrese la renta: "))
    tasa_capitalizable = float(input("Ingrese la tasa capitalizable (en porcentaje): "))
    periodo_capitalizacion = int(input("Ingrese el periodo de capitalización: "))
    # Calcular la anualidad vencida utilizando la fórmula proporcionada y redondearlo hacia arriba
    anualidad_vencida_calculada = calcular_anualidad_vencida(capital, renta, tasa_capitalizable, periodo_capitalizacion)
    # Calcular la nueva renta utilizando la fórmula proporcionada
    nueva_renta_calculada = calcular_nueva_renta(capital, tasa_capitalizable, anualidad_vencida_calculada)
    print(f"La anualidad vencida es: {anualidad_vencida_calculada} dias")
    print(f"La nueva renta es: {nueva_renta_calculada}")
elif opcion == 17:
    monto_prestamo = float(input("Ingrese el monto del préstamo: "))
    tasa_interes_anual = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
    numero_pagos = int(input("Ingrese el número de pagos: "))
    # Calcular la tabla de amortización
    tabla = calcular_amortizacion(monto_prestamo, tasa_interes_anual, numero_pagos)
    # Mostrar la tabla de amortización
    print("Tabla de Amortización:")
    print("Pago | Renta   | Amortización | Interés  | Saldo Insoluto")
    for fila in tabla:
        print(f"   {fila[0]} | {fila[1]} | {fila[2]}      | {fila[3]}    |  {fila[4]}")
else:
    print("Opción no válida")