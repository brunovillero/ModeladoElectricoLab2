k = 8987551788
E0 = 8.85e-12
from numpy import linalg, sqrt, pi, array

class cargaPuntual:
    def __init__(self, q, r):
        # Inicializa el valor de la carga q y la posición r=(x,y).
        self.q, self.r = q, array(r)
        
    def campo(self, r):
        # 1. Calculamos el vector distancia (r_evaluacion - r_carga)
        vector_distancia = array(r) - self.r
        
        # 2. Calculamos la distancia total (magnitud del vector)
        distanciaT = linalg.norm(vector_distancia)
        
        # 3. Evitamos la división por cero si el punto evaluado es exactamente la posición de la carga
        if distanciaT == 0:
            print("El campo en la posición exacta de la carga tiende al infinito.")
            return array([0.0, 0.0])
            
        # 4. Calculamos el campo eléctrico vectorial
        # Usamos k directamente como en el potencial, o bien (1/(4*pi*E0))
        # Multiplicamos por vector_distancia y dividimos por distanciaT al cubo
        campoElectrico = (k * self.q / (distanciaT**3)) * vector_distancia
        
        print(f"Campo electrico de carga en {self.r} hacia punto {r}:", campoElectrico)
        return campoElectrico
        
    def potencial(self, r):  
        distanciaT = linalg.norm(self.r - r)
        potencial = 0
        if distanciaT != 0:
            potencial = (k * self.q) / distanciaT
        return potencial