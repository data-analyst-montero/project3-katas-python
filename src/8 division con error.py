try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    resultado = num1 / num2

except ValueError:
    print("Error: Debes introducir valores numéricos.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
else:
    print(f"La división fue exitosa. Resultado: {resultado}")
finally:
    print("Fin del programa.")