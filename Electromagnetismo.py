'''
LIBRERIA ELECTROMAGNETISMO:
Es esta librería se define la clase Carga Puntual. La clase tiene como métodos el campo y potencial generado por ella en un punto dado. 
Pueden implementarse otros métodos o clases que se consideren de interés. 
'''
k=8987551788
E0 = 8.85e-12
from numpy import linalg, sqrt, pi, array
from Algebra import norm

class cargaPuntual:
    #radio = 0.01  # Radio de la carga
    def __init__(self, q, r):
        # Inicializa el valor de la carga q y la posición r=(x,y).
        self.q, self.r = q, array(r)
        
    def campo(self, r):
      distanciaX = r[0] - self.r[0]
      distanciaY = r[1] - self.r[1]
      signoCampoElectricoEnX = 1
      signoCampoElectricoEnY = 1
      if distanciaX < 0:
        signoCampoElectricoEnX = -1
      if distanciaY < 0:
        signoCampoElectricoEnY = -1    
      campoElectricoX = 0
      campoElectricoY = 0
      if distanciaX != 0:    
        campoElectricoX = (1/(4*pi*E0)) * (abs(self.q)) / (distanciaX**2)
      if distanciaY != 0:      
        campoElectricoY = (1/(4*pi*E0)) * (abs(self.q)) / (distanciaY**2)
      print("Campo electrico array:")
      print(array([campoElectricoX * signoCampoElectricoEnX, campoElectricoY * signoCampoElectricoEnY]))
      return array([campoElectricoX * signoCampoElectricoEnX, campoElectricoY * signoCampoElectricoEnY])
        
    def potencial(self, r):  
      distanciaT = linalg.norm(self.r - r)
      potencial = 0
      if distanciaT != 0:
        potencial = (k * self.q) / distanciaT
      return (potencial)      
