k = 8987551788
from numpy import linalg, sqrt, pi, array

class cargaPuntual:
    def __init__(self, q, r):
        # Inicializa el valor de la carga q y la posición r=(x,y).
        self.q, self.r = q, array(r)
        
    def campo(self, r):
      #r = array(r)
      diff = r - self.r
      distancia = linalg.norm(diff)
    
      if distancia == 0:
        return array([0.0, 0.0])
    
      mod_campo_elec = k * (self.q / distancia**2)
      u = diff / distancia
      
      campo_vectorial = mod_campo_elec * u
    
      print(f"Campo eléctrico en {r}: {campo_vectorial}")
      return campo_vectorial
        
    def potencial(self, r):  
        distanciaT = linalg.norm(self.r - r)
        potencial = 0
        if distanciaT != 0:
            potencial = (k * self.q) / distanciaT
        return potencial