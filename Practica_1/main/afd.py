#aca esta la clase donde revisa si cumple algunos de los parametros establecidos en la practica. Si una
#expresion es entero, real, notacion cientifica, complejo, palabra de interes o fecha.

#aca esta el AFD de la practica 3 de progra 2

class AFD():
#primero separamos el texto en palabras por espacios
    def __init__(self, profesion):
        self.es_palabra_de_interes = self.es_palabra_de_interes_matematica if profesion == 1 else self.es_palabra_de_interes_fisica
    def separar_palabras(self, texto):
        palabras = texto.split()
        return palabras

    def es_entero(self, palabra):     #azul
        try:
            temp = int(palabra)
            return True
        except:
            return False

    def es_real(self,palabra):       #verde
        try:
            if palabra - int(palabra) != 0:
                return True
            else:
                return False
        except:
            return False

    def es_notacion_cientifica(self,palabra):        #morado
        if 'E' in palabra:
            try:
                inicio = int(palabra[0:palabra.index('E')])
                final = int(palabra[palabra.index('E')+1:])
                return True
            except:
                return False


    def es_complejo(self,palabra):       #rojo
        if 'i' in palabra:
            pal_analizar = palabra[::-1]    #leer la palabra al reves para jugar con el simbolo i
            try:
                if '+' in palabra:
                    imaginaria = float(pal_analizar[1:pal_analizar.index('+')])
                    real = float(pal_analizar[pal_analizar.index('+')+1:])
                    return True
                if '-' in palabra:
                    imaginaria = float(pal_analizar[1:pal_analizar.index('-')])
                    real = float(pal_analizar[pal_analizar.index('-') + 1:])
                else:
                    imaginaria = float(pal_analizar[1:])
                    return True
            except:
                return False

    def es_palabra_de_interes_matematica(self,palabra):      #gris
        lista_palabras = ['teorema','Matemático','Matemática','Hilbert','Turing','análisis', 'Euler', 'Fermat',
                          'Pitágoras','autómata','Boole','Cantor','Perelman']
        if palabra in lista_palabras:
            return True
        else:
            return False

    def es_palabra_de_interes_fisica(self,palabra):      #gris
        lista_palabras = ['Experimentación','Físico','Física','Astronomía','Mecánica', 'Newton',
                          'Einstein','Galileo','Modelo','Tesla','Dinámica','Partículas']
        if palabra in lista_palabras:
            return  True
        else:
            return False

    def es_fecha(self,palabra):      #anaranjado
        if len(palabra) == 8 or len(palabra) == 10:
            if palabra[2] == palabra[5] == '/':
                fec = palabra.replace('/','')
                try:
                    int(fec)
                    return True
                except:
                    return False
            if palabra[2] == palabra[5] == '-':
                fec = palabra.replace('-','')
                try:
                    int(fec)
                    return True
                except:
                    return False
            if palabra[2] != palabra[5]:
                return False
        else:
            return False


    def colorizar(self, texto):
        palabras = self.separar_palabras(texto)
        resultados = ""

        for palabra in palabras:
            if self.es_entero(palabra):
                resultados += f" <span style='color:blue'>{palabra}</span>"
            if self.es_real(palabra):
                resultados += f" <span style='color:green'>{palabra}</span>"
            if self.es_notacion_cientifica(palabra):
                resultados += f" <span style='color:pruple'>{palabra}</span>"
            if self.es_complejo(palabra):
                resultados += f" <span style='color:red'>{palabra}</span>"
            if self.es_fecha(palabra):
                resultados += f" <span style='color:orange'>{palabra}</span>"
            if self.es_palabra_de_interes(palabra):
                resultados += f" <span style='color:grey'>{palabra}</span>"
            else:
                resultados += f' {palabra}'

        return resultados