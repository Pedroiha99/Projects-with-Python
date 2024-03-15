#Gráfica del Modelo de un Banco Óptico


import matplotlib.pyplot as plt
import numpy as np

distancia_objeto = [22, 23, 23, 25, 26.44, 27.2, 28.3, 29.4, 30.4, 31.4, 35.3, 34.4, 35.4, 35.5, 36.8, 38.3, 39.4, 40.5, 42.1, 43.3, 46.4, 46.9, 48.5, 49.6, 50.9, 52.2, 53.7, 55.4, 56.5, 57.9, 58.5, 60.4, 61, 63.1, 64, 65]
distancia_imagen = [32, 31, 28, 25.5, 24.3, 22.8, 23.4, 21, 23, 21.6, 21.5, 20.5, 20.3, 19.8, 19.3, 19.2, 19, 18.6, 18.1, 18.3, 17.5, 17.4, 17.2, 17, 16.6, 16, 16.1, 15.7, 16.2, 16.6, 16.1, 15.8, 15.5, 15.6, 15.9, 16.2 ]

saltos = 1000
datos = 36

lista_x = np.linspace(22, 65, saltos)
lista_y = [0] * saltos
lista_f = [0] * datos
lista_fx = np.linspace(22, 65, datos)

#linea de tendencia
def funcion_y(lista_x, lista_y):
    for i in range(saltos):
        lista_y[i] = 0.000000108365 * (lista_x[i]**6) - 0.0000299602 * (lista_x[i]**5) + 0.00339716 * (lista_x[i]**4) - 0.202041* (lista_x[i]**3) + 6.64783 * (lista_x[i]**2) - 115.099 * (lista_x[i]) + 844.324
    return lista_y

#ecuacion del fabricante, tambien f = do*di / do+di
def funcion_f(lista_f, distancia_objeto, distancia_imagen):
    for i in range(datos):
        lista_f[i] = 1/((1/distancia_objeto[i]) + (1/distancia_imagen[i]))
    return lista_f
    
lista_y = funcion_y(lista_x, lista_y)
lista_f = funcion_f(lista_f, distania_objeto, distancia_imagen)

titulo = ("Grafica de la distancia al objeto y la distancia a la imagen")
plt.xlabel("distancia objeto [cm]")
plt.ylabel("distancia imagen [cm]")
plt.plot(distancia_objeto, distancia_imagen, ".", label = "Puntos obtenidos experimentalmente.") 
plt.plot(lista_x, lista_y, label = "Linea de tendencia.")
plt.plot(lista_fx, lista_f, ".",label = "Foco de la lente en cada punto")
plt.legend()
plt.title(titulo)
plt.show()
 