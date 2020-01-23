import math
class complejo:
    '''
    Libreria de Numeros complejos, sera un objeto con atributos a, b , r y angle.
    Donde a y b con las componentes cartesianes ( a : parte real , b: parte imaginaria),
    r es el modulo , y angle es angulo theta en coordenadas polares,
    asi que cada representacion y atributos tendran que ser llamados de forma individual o pueden
    ser vistos de a parejas.
    Son INMUTABLES , por lo tanto una vez creados no se pueden modificar ninguno de sus atributos.
    '''
    def __init__(self, a=None, b=None,r=None,angle=None):
        '''
        El constructor de complejos, podra crear el objeto con coordenadas polares, o cartesianas,
        en cualquier caso seran calculados los atributos faltantes. En angulo debe ser en radianes y
        siempre el angulo sera calculado (o recalculado) en forma positiva de 0 a 2pi.
        Lanzara una excepcion si no se ha insertado parametros necesarios, cartesianos o polares.
        Si insertan todos los parametros ignorara los ultimos es decir , recalculara los polares.
        '''
        if(a != None and b!= None):
            self._a=a
            self._b=b
            self._r=math.sqrt(a**2+b**2)
            angle=math.atan2(b,a)
        elif(r!=None and angle!=None):
            self._r=r
            self._b=r*math.sin(angle)
            self._a=r*math.cos(angle)
        else:
            raise Exception("ERROR: Faltan Parametros")
        if (angle<0):
                angle=angle*-1
                angle=angle%(math.pi*2)
                angle=math.pi*2-angle
        self._angle=angle%(math.pi*2)

    @staticmethod
    def suma(x,y):
        '''
        Retorna la suma de dos complejos, creados como objetos.
        Lanzara excepcion si alguno de los no es un complejo
        Estatico, se podra llamar complejo.suma(x,y)
        '''
        complejo.soncomplejos(x,y)
        return complejo(x.a+y.a,x.b+y.b)

    @staticmethod
    def resta(x,y):
        '''
        Retorna la resta de dos complejos, creados como objetos.
        Lanzara excepcion si alguno de los no es un complejo
        Estatico, se podra llamar complejo.resta(x,y)
        '''
        complejo.soncomplejos(x,y)
        return complejo(x.a-y.b,x.b-y.b)

    @staticmethod
    def producto(x, y):
        '''
        Retorna el producto de dos complejos, creados como objetos.
        Lanzara excepcion si alguno de los no es un complejo
        Estatico, se podra llamar complejo.producto(x,y)
        '''
        complejo.soncomplejos(x,y)
        return complejo(x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a)

    @staticmethod
    def division(x, y):
        '''
        Retorna la division de dos complejos, creados como objetos.
        Lanzara excepcion si alguno de los no es un complejo, y
        si el divisor resulta ser 0. (Zero Div Error)
        Estatico, se podra llamar complejo.division(x,y)
        '''
        complejo.soncomplejos(x,y)
        z=y.conjugado()
        n=complejo.producto(x,z)
        try:
            d=(y.a**2+y.b**2)
            ans=complejo(n.a/d,n.b/d)
            return ans
        except ZeroDivisionError as e:
            raise Exception("ERROR: Division por 0")

    @staticmethod
    def potencia(x,n):
        '''
        Retorna la potencia de un numero complejo, creado como objeto.
        Lanzara excepcion si x no es un complejo.
        n debe ser real
        Estatico, se podra llamar complejo.producto(x,y)
        '''
        if(not isinstance(x, complejo)):
            raise Exception("ERROR: Deben se Complejo el numero a elevar")
        return complejo(r=x.r**n,angle=n*x.angle)

    def conjugado(self):
        '''
        Retorna el conjugado de un numero complejo,
        se podra lamar como el_numero.complejo()
        '''
        return complejo(self.a,-self.b)

    def pcartesiana(self):
        '''
        Imprime de la forma cartesiana a + ib el numero complejo
        '''
        x=str("%.3f" % self.a)
        y=""
        if(self.b>0):
            y="+"
        print(x+y+"%.3f" % self.b+"i")

    def ppolar(self):
        '''
        Imprime de la forma polar (r, angulo θ)
        '''
        print("("+str("%.3f" % self.r)+","+"%.5f" % self.angle+" θ )")


    def __str__(self):
        '''
        Override para usar print, predeterminadamente al hacerle print al
        numero complejo lo imprimira como la dupla (a,b)
        '''
        return "("+str(self.a)+", "+str(self.b)+")"

    @property
    def r(self):
        '''
        Get de r , devuelve el modulo, se podra utilizar:
        el_numero.r
        '''
        return self._r

    @property
    def a(self):
        '''
        Get de a , devuelve la parte real, se podra utilizar:
        el_numero.a
        '''
        return self._a

    @property
    def b(self):
        '''
        Get de b , devuelve la parte imaginaria, se podra utilizar:
        el_numero.b
        '''
        return self._b

    @property
    def angle(self):
        '''
        Get de angle , devuelve el angulo, se podra utilizar:
        el_numero.angle
        '''
        return self._angle

    @staticmethod
    def soncomplejos(x,y):
        '''
        Hace la verificacion de tipos, lanzara una excepcion si alguno de los parametros
        x o y no es un complejo
        Estatico , se podar usar complejos.soncomplejos(x,y)
        '''
        if (not isinstance(x, complejo) or not isinstance(y, complejo)) :
            raise Exception("ERROR: Deben ser Complejos los Parametros")
