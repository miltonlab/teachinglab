import numpy

distancias = numpy.array([[0,2050, 2015, 2190, 2725],
[2050, 0, 119, 140, 675],
[2015, 119, 0, 255, 790],
[2190, 140, 255, 0, 535],
[2725, 675, 790, 535, 0]])
ciudades = numpy.array(['Arica', 'Santiago', 
'Valparaiso', 'San Fernando', 'Temuco'])

def ingresar_itinerario():
	num_ciudades = input("Ingrese el numero de ciudades del itinerario: ")
	num_ciudades = int(num_ciudades)
	itinerario = []
	print("Ingrese las ciudades del itinerario: ")
	for c in range(0, num_ciudades):
		itinerario.append(input())
	return itinerario
	

def kms(itinerario):
	# Calculo de las distancias del itinerario
	d = 0
	num_ciudades = len(itinerario)
	for t in range(0, num_ciudades -1):
		c1 = -1
		c2 = -1
		# Buscamos el índice que le corresponde a 
		# la  primera ciudad (origen) 
		for c in range(0,len(ciudades)):
<<<<<<< HEAD
		    if ciudades[c] == itinerario[t]:
		        c1 = c
                print ('es igual c1')
		    if ciudades[c] == itinerario[t+1]:
		        c2 = c
				print('es igual c2')
=======
			if ciudades[c] == itinerario[t]:
				c1 = c
				break
		# Buscamos el índice que le corresponde a 
		# la segunda ciudad (destino)
		for c in range(0,len(ciudades)):
			if ciudades[c] == itinerario[t+1]:
				c2 = c
				break
>>>>>>> 02ac62df9636a408e53f556e08b8132250c1f9ae
		d = d + distancias[c1][c2]
		print (ciudades[c1], '-', ciudades[c2], distancias[c1][c2])
	print('La distancia total es: ', d)

itinerario = ingresar_itinerario()
kms(itinerario)

# Ejecucion:
# pyton examenedd1.py
# Ingrese el numero de ciudades del itinerario: 4
# Ingrese las ciudades del itinerario: 
# Temuco
# Santiago
# San Fernando
# Arica
# Temuco - Santiago 675
# Santiago - San Fernando 140
# San Fernando - Arica 2190
# La distancia total es:  3005

