from libreriacomplejos import complejo as C
import math
def test_sum():
    uno=C.suma(C(1,-6),C(-4,-4))
    dos=C.suma(C(1.568546,-1.6556448),C(-1.58987,-1.46549687))
    tres=C.suma(C(600,-400),C(400,400))
    assert uno.a==-3 and uno.b==-10 , "Los resultados: "+str(uno.a)+","+str(uno.b)
    assert math.isclose(dos.a, -0.021324, rel_tol=1e-5) and \
    math.isclose(dos.b, -3.12114  , rel_tol=1e-5) \
    , "Los resultados : "+str(dos.a)+","+str(dos.b)
    assert tres.a==1000 and tres.b==0, "Los resultados : "+str(tres.a)+","+str(tres.b)

def test_res():
    uno=C.resta(C(1,-6),C(-4,-4))
    dos=C.resta(C(1.568546,-1.6556448),C(-1.58987,-1.46549687))
    tres=C.resta(C(600,-400),C(400,400))
    assert uno.a==5 and uno.b==-2 , "Los resultados: "+str(uno.a)+","+str(uno.b)
    assert math.isclose(dos.a, 3.15842, rel_tol=1e-5) and \
    math.isclose(dos.b, -0.190148  , rel_tol=1e-5) \
    , "Los resultados : "+str(dos.a)+","+str(dos.b)
    assert tres.a==200 and tres.b==-800, "Los resultados : "+str(tres.a)+","+str(tres.b)

def test_producto():
    uno=C.producto(C(1,-6),C(-4,-4))
    dos=C.producto(C(1.568546,-1.6556448),C(-1.58987,-1.46549687))
    tres=C.producto(C(600,-400),C(400,400))
    assert uno.a==-28 and uno.b==20 , "Los resultados: "+str(uno.a)+","+str(uno.b)
    assert math.isclose(dos.a, -4.92013, rel_tol=1e-5) and \
    math.isclose(dos.b, 0.333561 , rel_tol=1e-5) \
    , "Los resultados : "+str(dos.a)+","+str(dos.b)
    assert tres.a==400000 and tres.b==80000, "Los resultados : "+str(tres.a)+","+str(tres.b)

def test_division():
    uno=C.division(C(1,-6),C(-4,-4))
    dos=C.division(C(1.568546,-1.6556448),C(-1.58987,-1.46549687))
    tres=C.division(C(600,-400),C(400,400))
    assert uno.a==0.625 and uno.b==0.875 , "Los resultados: "+str(uno.a)+","+str(uno.b)
    assert math.isclose(dos.a, -0.0144250, rel_tol=1e-5) and \
    math.isclose(dos.b, 1.05467   , rel_tol=1e-5) \
    , "Los resultados : "+str(dos.a)+","+str(dos.b)
    assert tres.a==0.25 and tres.b==-1.25, "Los resultados : "+str(tres.a)+","+str(tres.b)

def test_potencia():
    uno=C.potencia(C(2,-2),5)
    dos=C.potencia(C(2,-2),6)
    tres=C.potencia(C(2,-2),7)
    cuatro=C.potencia(C(2,-2),8)
    assert uno.a==-128 and uno.b==128, "Los resultados: "+str(uno.a)+","+str(uno.b)
    assert dos.a==0 and dos.b==512, "Los resultados: "+str(dos.a)+","+str(dos.b)
    assert tres.a==1024 and tres.b==1024, "Los resultados: "+str(tres.a)+","+str(tres.b)
    assert cuatro.a==4096 and cuatro.b==0, "Los resultados: "+str(cuatro.a)+","+str(cuatro.b)

def test_conjugado():
    uno=C(2,-2).conjugado()
    dos=C(3,2).conjugado()
    assert uno.a==2 and uno.b==2, "Los resultados: "+str(uno.a)+","+str(uno.b)
    assert dos.a==3 and dos.b==-2, "Los resultados: "+str(dos.a)+","+str(dos.b)

def test_polar():
    uno=C(2,-2)
    dos=C(-3,-3)
    tres=C(4,4)
    cuatro=C(-5,5)
    assert math.isclose(uno.r, 2.82843, rel_tol=1e-5) and \
    math.isclose(uno.angle, 5.4977871437  , rel_tol=1e-5) \
    , "Los resultados : "+str(uno.r)+","+str(uno.angle)
    assert math.isclose(dos.r, 4.24264, rel_tol=1e-5) and \
    math.isclose(dos.angle, 3.9269908169  , rel_tol=1e-5) \
    , "Los resultados : "+str(dos.r)+","+str(dos.angle)
    assert math.isclose(tres.r, 5.65685, rel_tol=1e-5) and \
    math.isclose(tres.angle, 0.78539816  , rel_tol=1e-5) \
    , "Los resultados : "+str(tres.r)+","+str(tres.angle)
    assert math.isclose(cuatro.r, 7.07107, rel_tol=1e-5) and \
    math.isclose(cuatro.angle, 2.356194490  , rel_tol=1e-5) \
    , "Los resultados : "+str(cuatro.r)+","+str(cuatro.angle)

def test_cartesiana():
    uno=C(r=2.82843,angle=5.4977871437)
    dos=C(r=4.24264,angle=3.9269908169)
    tres=C(r=5.65685,angle=0.78539816 )
    cuatro=C(r=7.07107,angle=2.356194490)
    assert math.isclose(uno.a, 2, rel_tol=1e-5) and \
    math.isclose(uno.b, -2  , rel_tol=1e-5) \
    , "Los resultados : "+str(uno.a)+","+str(uno.b)
    assert math.isclose(dos.a, -3, rel_tol=1e-5) and \
    math.isclose(dos.b, -3  , rel_tol=1e-5) \
    , "Los resultados : "+str(dos.a)+","+str(dos.b)
    assert math.isclose(tres.a, 4, rel_tol=1e-5) and \
    math.isclose(tres.b, 4  , rel_tol=1e-5) \
    , "Los resultados : "+str(tres.a)+","+str(tres.b)
    assert math.isclose(cuatro.a, -5, rel_tol=1e-5) and \
    math.isclose(cuatro.b, 5  , rel_tol=1e-5) \
    , "Los resultados : "+str(cuatro.a)+","+str(cuatro.b)

if __name__ == "__main__":
    test_sum()
    test_res()
    test_producto()
    test_division()
    test_potencia()
    test_conjugado()
    test_polar()
    test_cartesiana()
    print("Pruebas Existosas ")
