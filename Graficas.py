'''
LIBRERIA GRÁFICAS:
Es esta librería se definen las funciones necesarias para poder graficar los distintos componentes de interés. 
'''

from matplotlib import pyplot
from numpy import sqrt, fabs, array, exp, pi, arctan2
from Electromagnetismo import cargaPuntual
from Algebra import norm
from Algebra import angulo

#-----------------------------------------------------------------------------
# Dimensiones del plano en donde se graficarán las cargas. Inicialmente se declaran en None para luego ser completadas con valores dados en la incialización del programa
XMIN, XMAX = None, None
YMIN, YMAX = None, None
ZOOM = None
XOFFSET = None

#Se establece valor para la constante k
k=8987551788 #Nm^2/C^2
#-----------------------------------------------------------------------------
# Funciones para iniciar y ajustar el gráfico. 

def iniciarGrafico(xmin, xmax, ymin, ymax, zoom=1, xoffset=0):
    #Iniciar el gráfico 
    global XMIN, XMAX, YMIN, YMAX, ZOOM, XOFFSET
    XMIN, XMAX, YMIN, YMAX, ZOOM, XOFFSET = \
      xmin, xmax, ymin, ymax, zoom, xoffset

def ajustarGráfico():
    # Finalizar el gráfico
    ax = pyplot.gca()
    ax.set_xticks([])
    ax.set_yticks([])
    pyplot.xlim(XMIN/ZOOM+XOFFSET, XMAX/ZOOM+XOFFSET)
    pyplot.ylim(YMIN/ZOOM, YMAX/ZOOM)
    pyplot.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)

#-----------------------------------------------------------------------------
#Funciones que ingresan las formas gráficas de cada elemento en la figura. 
        
def graficarCargaPuntual(carga):
  # Genera un punto de color (donde el color indica el signo de la carga)
    color = 'b' if carga.q < 0 else 'r' if carga.q > 0 else 'k'
    # El radio del punto se calcula en base al valor de la carga, para que cargas de mayor valor se vean más grandes. 
    # La ecuación utilizada fue considerada razonable, pero el desarrollador puede modificarla para obtener el resultado que se ajuste a sus gustos. 
    r = 0.05*(sqrt(fabs(carga.q))/2 + 1)
    circle = pyplot.Circle(carga.r, r, color=color, zorder = 10)
    pyplot.gca().add_artist(circle)

def CalcularCampos(listaDeCargas, medida, Campos):
#Se suman los campos de todas las cargas
  campo = sum([carga.campo(medida) for carga in listaDeCargas ])
#Se calcula el módulo del campo a partir de los componentes en x e y
  Campos.append(sqrt(campo[0]**2+campo[1]**2))

def graficarMedidaDeCampo(listaDeCargas, medida, MaxCampo):
#Se suman los campos de todas las cargas
  campo = sum([carga.campo(medida) for carga in listaDeCargas ])
#Se calcula el módulo del campo a partir de los componentes en x e y
  E = sqrt(campo[0]**2+campo[1]**2)
#Se caclula el angulo usando arcotangente
  angle = arctan2(campo[1],campo[0])*180/pi
#si el angulo es muy chico, se toma 0
  if abs(angle) <0.001:
     angle=0
#Muestra toda la información previamente calculada
  print("Campo en (" + f"{medida[0]:.3g}" + ", " + f"{medida[1]:.3g}" + ") = " + f"{E:.3g}" + " V/m con " + f"{angle:.3g}" + "°/s")
#Cambio escala de puntos para que se vea mejor
  campo = campo/MaxCampo
  escala = 1
#Grafico
  pyplot.gca().quiver(array(medida[0]),array(medida[1]),array(campo[0]),array(campo[1]),units='xy',scale=escala,color='k')

#-----------------------------------------------------------------------------
#Functiones para agregar elementos a graficar

def agregarCarga(listaDeCargas, carga = 1, x = 0, y = 0) -> cargaPuntual:
  # Esta función agrega una carga de valor q en la posición (x,y).
  # Se debe pasar como parámentro la lista de cargas obtenida de la función iniciar() así como los parámentros de la carga.  
  nuevaCarga = cargaPuntual(carga, [x, y])
  listaDeCargas.append(nuevaCarga)
  # La función retorna el elemento creado de la clase cargaPuntual
  return nuevaCarga

def agregarMedidaDeCampo(listaDeMedidas, x = 0, y = 0 ):
  # Esta función agrega una posición (x,y) a la lista de medidas de Campo a realizar.  
  listaDeMedidas.append([x,y])

def AgregarMedidaDePotencial(listamed,x,y): 
  # Esta función agrega una posición (x,y) a la lista de medidas de Potencial realizar. 
  listamed.append([x,y])

# Esta funcion suma los potenciales de cada carga en la lista en el punto med
def calcularPotencial(med,listaCargas): 
  Volt=0 
  for carga in listaCargas: 
    Volt+=carga.potencial(med) 
  #Display de la información. Muestra en 3 cifras
  print("Potencial en ("+ f"{med[0]:.3g}" + ", " + f"{med[1]:.3g}" + ") = ",f"{Volt:.3g}","V")
#La otra función que creamos completamente es calcularpotencial(), la cual toma un valor med, que representa la lista de la posición x e y que agregamos en AgregarMedidaDePotencial, y la lista de Cargas. Esta función llama al método de la carga el cual calcula el potencial y suma todos los potenciales de todas las cargas creadas para luego imprimir su valor en la consola. 


#Esta funcion inicia las variables requeridas
def iniciar(L):
  XMIN, XMAX = -2*L, 2*L 
  YMIN, YMAX = -2*L, 2*L 
  ZOOM = 1 
  XOFFSET = 0 
  iniciarGrafico(XMIN, XMAX, YMIN, YMAX, ZOOM, XOFFSET) 
  cargas = [] 
  medidas = [] 
  listamed = [] 
  return (cargas, medidas, listamed) 

#esta funcion grafica todo lo requerido
def mostrar(cargas = None, medidas = None,listamed= None): 
  pyplot.figure(figsize=(4, 4)) 
  ajustarGráfico() 
  [graficarCargaPuntual(carga) for carga in cargas] 
  CampoModulos = []
  [CalcularCampos(cargas,medida,CampoModulos) for medida in medidas]
  MaxCampo = max(CampoModulos)
  if MaxCampo == 0:
    MaxCampo = 1
  [graficarMedidaDeCampo(cargas,medida,MaxCampo) for medida in medidas] 
  for med in listamed: 
    calcularPotencial(med,cargas) 
  pyplot.show()