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

# Obtener los valores necesarios para el cálculo
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
