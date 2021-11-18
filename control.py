import threading
from clases import bandeja, PI_simple


bandejas=[bandeja(0,1,1),bandeja(0,1,1),bandeja(0,1,1),bandeja(0,1,1),bandeja(0,1,1),bandeja(0,1,1),bandeja(0,1,1),bandeja(0,1,1)]

def control():
    print('holiii')

    controlador=PI_simple()

    for i in bandejas:

        if i.estado==0:
            continue
        else:
            controlador.update(i.temperatura(), i.semilla[1])

            controlador.update(i.humedad(), i.semilla[2])


    threading.Timer(5.0, control).start()
