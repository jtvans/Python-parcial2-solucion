distancia_sujeto1 = float(input("Distancia en metros para Sujeto 1: "))
tiempo_sujeto1 = float(input("Tiempo en segundos para Sujeto 1: "))
velocidad_sujeto1 = distancia_sujeto1 / tiempo_sujeto1

print("\n")

distancia_sujeto2 = float(input("Distancia en metros para Sujeto 2: "))
tiempo_sujeto2 = float(input("Tiempo en segundos para Sujeto 2: "))
velocidad_sujeto2 = distancia_sujeto2 / tiempo_sujeto2

print("\n")


if velocidad_sujeto1 > velocidad_sujeto2:
    print("Sujeto 1 camina más rápido.")
elif velocidad_sujeto2 > velocidad_sujeto1:
    print("Sujeto 2 camina más rápido.")
else:
    print("Ambos sujetos caminan a la misma velocidad.")

print(f"Velocidad Sujeto 1: {velocidad_sujeto1:.2f} m/s")
print(f"Velocidad Sujeto 2: {velocidad_sujeto2:.2f} m/s")

