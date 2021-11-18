import mcp3008
def obtener_humedad(i):
    ch0=mcp3008.sensores()
    print(ch0.humedad(i))
    print(ch0.temperatura())
    
obtener_humedad(6)
    
    