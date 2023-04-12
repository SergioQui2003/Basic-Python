# determinamos el problema el salario a pagar a un empleado, teniendo como entradas el salario diario y el número de días trabajados

sueldo_diario = float(input("Ingrese cuanto gana diariamente: "))
dias_de_trabajo = int(input("Ingrese cuantos dias trabaja: "))

# Descontamos del sueldo lo de pensiones y lo de salud 
subtotal = sueldo_diario * dias_de_trabajo
descuento_de_pension = 0.10 * subtotal
descuento_de_salud = 0.15 * subtotal
descuento_total = descuento_de_pension + descuento_de_salud

# hacemos la formula para que nos el total del salario del empleador 
salario = subtotal - descuento_total

print("El salario a pagar al empleador es de:", salario)