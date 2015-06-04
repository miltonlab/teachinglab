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
	# itineario puede ser un list
	# itemsize indica el tamaño de las palabras
	itinerario = numpy.chararray(num_ciudades, itemsize=15)
	print("Ingrese las ciudades del itinerario: ")
	for c in range(0, num_ciudades):
		itinerario[c] = input()
	print(itinerario)
	return itinerario
	

def kms(itinerario):
	# Calculo de las distancias del itinerario
	d = 0
	num_ciudades = len(itinerario)
	for t in range(0, num_ciudades -1):
		print ('bucle')
		c1 = -1
		c2 = -1
		# Buscamos el índice que le corresponde a 
		# la ciudad del itinerario en la lista de ciudades
		for c in range(0,len(ciudades)):
		    if ciudades[c] == itinerario[t]:
		        c1 = c
		    if ciudades[c] == itinerario[t+1]:
		        c2 = c
		d = d + distancias[c1][c2]
		print (ciudades[c1], '-', ciudades[c2], distancias[c1][c2])
	print('La distancia total es: ', d)

itinerario = ingresar_itinerario()
kms(itinerario)
