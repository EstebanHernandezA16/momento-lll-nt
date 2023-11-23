import pandas as pd
import matplotlib.pyplot as plt


clientes_df = pd.read_csv('clientes.csv')
productos_df = pd.read_csv('productos.csv')
pedidos_df = pd.read_csv('pedidos.csv')


sumar = lambda columna: columna.sum()
promedio = lambda columna: columna.mean()
maximo = lambda columna: columna.max()
minimo = lambda columna: columna.min()

# Edades de clientes
plt.hist(clientes_df['edad'], bins=10, edgecolor='black')
plt.xlabel('Edades')
plt.ylabel('Veces que se repite cada edad')
plt.title('Distribución de Edades de los Clientes')
plt.show()

plt.scatter(clientes_df['genero'], clientes_df['edad'])
plt.xlabel('Precio del Producto')
plt.ylabel('Cantidad Vendida')
plt.title('Relación entre Precio y Cantidad de Productos Vendidos')
plt.show()


productos_vendidos_por_cliente = sumar(pedidos_df.groupby('id_cliente')['cantidad'])
productos_vendidos_por_cliente.plot(kind='bar')
plt.xlabel('ID del Cliente')
plt.ylabel('Cantidad de Productos Vendidos')
plt.title('Cantidad de Productos Vendidos por Cliente')
plt.show()


clientes_df['genero'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Proporción de Géneros de Clientes')
plt.show()
