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
plt.hist(clientes_df['edad'], bins=20, edgecolor='black')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.title('Distribución de Edades de los Clientes')
plt.show()

# Gráfico de barras para la cantidad de productos por categoría
productos_df['categoria'].value_counts().plot(kind='bar')
plt.xlabel('Categoría')
plt.ylabel('Cantidad de Productos')
plt.title('Cantidad de Productos por Categoría')
plt.show()

# Grafico 3: Gráfico de dispersión para la relación entre precio y cantidad de productos vendidos
plt.scatter(productos_df['precio'], pedidos_df['cantidad'])
plt.xlabel('Precio del Producto')
plt.ylabel('Cantidad Vendida')
plt.title('Relación entre Precio y Cantidad de Productos Vendidos')
plt.show()

# Grafico 4: Gráfico de barras para la cantidad de productos vendidos por cliente
productos_vendidos_por_cliente = pedidos_df.groupby('id_cliente')['cantidad'].sum()
productos_vendidos_por_cliente.plot(kind='bar')
plt.xlabel('ID del Cliente')
plt.ylabel('Cantidad de Productos Vendidos')
plt.title('Cantidad de Productos Vendidos por Cliente')
plt.show()

# Grafico 5: Gráfico de pastel para la proporción de géneros de clientes
clientes_df['genero'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Proporción de Géneros de Clientes')
plt.show()
