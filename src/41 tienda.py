# Solicitar precio del artículo
precio_original = float(input("Introduce el precio original del artículo: "))

# Preguntar si tiene cupón
cupon = input("¿Tienes un cupón de descuento? (si/no): ").lower()

precio_final = precio_original

if cupon == "si":
    descuento = float(input("Introduce el valor del descuento del cupón: "))

    if descuento > 0:
        precio_final = precio_original - descuento
        print(f"Se aplicó un descuento de {descuento}€.")
    else:
        print("El valor del cupón no es válido. No se aplica descuento.")

elif cupon == "no":
    print("No se aplicará ningún descuento.")

else:
    print("Respuesta no válida. No se aplicará descuento.")

# Mostrar precio final
if precio_final < 0:
    precio_final = 0

print(f"El precio final de la compra es: {precio_final}€")