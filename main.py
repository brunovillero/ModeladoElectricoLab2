import Graficas as gr

# Define el valor de la carga
Q=1*1e-6

# Define la distancia mas larga a utilizar
L=2

#Inicializa el grafico
cargas, medidas,listamed = gr.iniciar(L)

#Parte A
#Agregar todas las cargas aca
#gr.agregarCarga(cargas,-10*Q,-1,-1)
#gr.agregarCarga(cargas,+6*Q,-1,+1)
#gr.agregarCarga(cargas,+6*Q,+1,-1)

#Agregar los puntos donde se debe graficar los campos
#gr.agregarMedidaDeCampo(medidas,0,0)
#gr.agregarMedidaDeCampo(medidas,1,1)
#gr.agregarMedidaDeCampo(medidas,0,L/2)

#Agregar los puntos donde se debe calcular el potencial
#gr.AgregarMedidaDePotencial(listamed,0,0)
#gr.AgregarMedidaDePotencial(listamed,1,1)

#Parte B.1
#gr.agregarCarga(cargas,Q/2,0,0)
#gr.agregarCarga(cargas,Q/2,0,L*2)
#Medidas de campo electrico
#gr.agregarMedidaDeCampo(medidas,L/4,0)
#gr.agregarMedidaDeCampo(medidas,L/4,L/8)
#gr.agregarMedidaDeCampo(medidas,L,0)
#gr.agregarMedidaDeCampo(medidas,L/4,-L/8)
#gr.agregarMedidaDeCampo(medidas,L/2,0)
#Medidas de potencial
#gr.AgregarMedidaDePotencial(listamed,L/4,0)
#gr.AgregarMedidaDePotencial(listamed,L/4,L/8)
#gr.AgregarMedidaDePotencial(listamed,L,0)
#gr.AgregarMedidaDePotencial(listamed,L/4,-L/8)
#gr.AgregarMedidaDePotencial(listamed,L/2,0)


#Parte B.2
#gr.agregarCarga(cargas,Q/3,0,0)
#gr.agregarCarga(cargas,Q/3,0,L)
#gr.agregarCarga(cargas,Q/3,0,L*2)
#Medidas de campo electrico
#gr.agregarMedidaDeCampo(medidas,L/4,0)
#gr.agregarMedidaDeCampo(medidas,L/4,L/8)
#gr.agregarMedidaDeCampo(medidas,L,0)
#gr.agregarMedidaDeCampo(medidas,L/4,-L/8)
#gr.agregarMedidaDeCampo(medidas,L/2,0)
#Medidas de potencial
#gr.AgregarMedidaDePotencial(listamed,L/4,0)
#gr.AgregarMedidaDePotencial(listamed,L/4,L/8)
#gr.AgregarMedidaDePotencial(listamed,L,0)
#gr.AgregarMedidaDePotencial(listamed,L/4,-L/8)
#gr.AgregarMedidaDePotencial(listamed,L/2,0)

#Parte B.3
#gr.agregarCarga(cargas,Q/5,0,0)
#gr.agregarCarga(cargas,Q/5,0,L/2)
#gr.agregarCarga(cargas,Q/5,0,L)
#gr.agregarCarga(cargas,Q/5,0,3*L/2)
#gr.agregarCarga(cargas,Q/5,0,L*2)
#Medidas de campo electrico
#gr.agregarMedidaDeCampo(medidas,L/4,0)
#gr.agregarMedidaDeCampo(medidas,L/4,L/8)
#gr.agregarMedidaDeCampo(medidas,L,0)
#gr.agregarMedidaDeCampo(medidas,L/4,-L/8)
#gr.agregarMedidaDeCampo(medidas,L/2,0)
#Medidas de potencial
#gr.AgregarMedidaDePotencial(listamed,L/4,0)
#gr.AgregarMedidaDePotencial(listamed,L/4,L/8)
#gr.AgregarMedidaDePotencial(listamed,L,0)
#gr.AgregarMedidaDePotencial(listamed,L/4,-L/8)
#gr.AgregarMedidaDePotencial(listamed,L/2,0)


# --- Ejercicio Entregable ---
Q1 = -15 * 1e-6
Q2 = 5 * 1e-6
Q3 = 5 * 1e-6

gr.agregarCarga(cargas, Q1, -2, -2)
gr.agregarCarga(cargas, Q2, -2, 2)
gr.agregarCarga(cargas, Q3, 2, -2)

# Potencial y Campo en origen (0,0) y en (2,2)
#gr.AgregarMedidaDePotencial(listamed, 0, 0)
gr.AgregarMedidaDePotencial(listamed, 2, 2)
#gr.agregarMedidaDeCampo(medidas, 0, 0)
gr.agregarMedidaDeCampo(medidas, 2, 2)

#Mostrar el resultado
gr.mostrar(cargas, medidas,listamed)