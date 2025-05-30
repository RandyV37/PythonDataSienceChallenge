# -*- coding: utf-8 -*-
"""AluraStoreLatam.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mevW11triJXBhGbMlnKuOkZcl-OlbgRx

### Importación de datos
"""

import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda.head()
tienda2.head()
tienda3.head()
tienda4.head()

"""#1. Análisis de facturación


"""

ingresos = {
    "Tienda 1": tienda["Precio"].sum(),
    "Tienda 2": tienda2["Precio"].sum(),
    "Tienda 3": tienda3["Precio"].sum(),
    "Tienda 4": tienda4["Precio"].sum()
}

for tienda, ingreso in ingresos.items():
    print(f"{tienda}: ${ingreso:,.0f}")

plt.figure(figsize=(10, 6))
plt.bar(ingresos.keys(), ingresos.values(), color=['skyblue', 'salmon', 'limegreen', 'orange'])
plt.title("Ingresos Totales por Tienda")
plt.xlabel("Tiendas")
plt.ylabel("Ingresos en pesos")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

"""# 2. Ventas por categoría"""

print("\nProductos vendidos por categoría - Tienda 1")
print(tienda["Categoría del Producto"].value_counts())

print("\nProductos vendidos por categoría - Tienda 2")
print(tienda2["Categoría del Producto"].value_counts())

print("\nProductos vendidos por categoría - Tienda 3")
print(tienda3["Categoría del Producto"].value_counts())

print("\nProductos vendidos por categoría - Tienda 4")
print(tienda4["Categoría del Producto"].value_counts())

"""# 3. Calificación promedio de la tienda

"""

promedios = {
    "Tienda 1": tienda["Calificación"].mean(),
    "Tienda 2": tienda2["Calificación"].mean(),
    "Tienda 3": tienda3["Calificación"].mean(),
    "Tienda 4": tienda4["Calificación"].mean()
}

for tienda, promedio in promedios.items():
    print(f"{tienda}: {promedio:.2f}")

plt.figure(figsize=(10, 6))
plt.plot(list(promedios.keys()), list(promedios.values()), marker='o', linestyle='-', color='blue')
plt.title("Calificación promedio de los clientes por tienda")
plt.xlabel("Tiendas")
plt.ylabel("Calificación promedio")
plt.ylim(0, 5)
plt.grid(True)
plt.tight_layout()
plt.show()

"""# 4. Productos más y menos vendidos"""

def analizar_ventas(df, nombre_tienda):
    conteo = df["Producto"].value_counts()
    mas_vendido = conteo.idxmax()
    menos_vendido = conteo.idxmin()

    print(f"\n{nombre_tienda}")
    print(f"Producto más vendido: {mas_vendido} ({conteo.max()} unidades)")
    print(f"Producto menos vendido: {menos_vendido} ({conteo.min()} unidades)")
    print("\nTop 5 productos más vendidos:")
    for producto, cantidad in conteo.head(5).items():
      print(f"{producto}: {cantidad} unidades")
    print("\nTop 5 productos menos vendidos:")
    for producto, cantidad in conteo.tail(5).items():
      print(f"{producto}: {cantidad} unidades")

# Aplicar análisis a cada tienda
analizar_ventas(tienda, "Tienda 1")
analizar_ventas(tienda2, "Tienda 2")
analizar_ventas(tienda3, "Tienda 3")
analizar_ventas(tienda4, "Tienda 4")

"""# 5. Envío promedio por tienda"""

promedio_envio = {
    "Tienda 1": tienda["Costo de envío"].mean(),
    "Tienda 2": tienda2["Costo de envío"].mean(),
    "Tienda 3": tienda3["Costo de envío"].mean(),
    "Tienda 4": tienda4["Costo de envío"].mean()
}

print("Costo de envío promedio por tienda:")
for tienda, costo in promedio_envio.items():
    print(f"{tienda}: ${costo:.2f}")

tiendas = list(promedio_envio.keys())
costos = list(promedio_envio.values())
colores = ['skyblue', 'lightgreen', 'salmon', 'plum']

plt.figure(figsize=(8, 5))
bars = plt.bar(tiendas, costos, color=colores)
plt.title("Costo de Envío Promedio por Tienda")
plt.ylabel("Costo Promedio ($)")
plt.xlabel("Tienda")

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f"${yval:.2f}", ha='center', va='bottom')

plt.tight_layout()
plt.show()