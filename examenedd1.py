class Pila: 
    top = None 

    def __init__(self): 
        self.sig = None 
        self.dato = None

    def push(self, dato): 
        nuevo = Pila() 
        nuevo.dato = dato 
        nuevo.sig = Pila.top 
        Pila.top = nuevo 

    def pop(self): 
        if self.vacia(): 
            print("No hay elementos en la pila")
        else: 
            Pila.top = Pila.top.sig 
            return Pila.top.dato

    def vacia(self): 
        if Pila.top == None: 
            return True 
        else: 
            return False 

    def imprimir(self): 
        tmp = Pila.top 
        while tmp != None: 
            if tmp.sig != None:
                print (tmp.dato)
            else:
                print (tmp.dato)
            tmp = tmp.sig

    def longitud(self):
        contador = 0
        tmp = Pila.top 
        while tmp != None: 
            tmp = tmp.sig
            contador = contador + 1
        return contador

p = Pila()
p.push(4)
p.push(5)
p.push(45)
p.imprimir()
print('El tamaño de la pila es: ', p.longitud())
p.pop()
p.imprimir()
print('El tamaño de la pila es: ', p.longitud())
