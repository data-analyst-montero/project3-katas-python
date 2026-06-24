try:
    edad = int(input("Introduce tu edad: "))

    if edad < 0 or edad > 120:
        raise ValueError

except ValueError:
    print("Error: Debes introducir una edad válida entre 0 y 120 años.")

else:
    print(f"Edad registrada correctamente: {edad} años.")