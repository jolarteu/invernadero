from clases import bandeja, PI_simple
import time

chl=[bandeja(0,1,1), bandeja()]
time.sleep(1)
print(chl[0].humedad())
print(chl[0].temperatura())
print(chl[1].estado)

chl[1].estado=0
print(chl[1].estado)

def control():
    
    controlador=PI_simple()
    
    for i in chl:
    
        controlador.update(i.temperatura(), i.semilla[1])
        print('cambio')
        controlador.update(i.humedad(), i.semilla[2])

    
