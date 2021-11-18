import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from w1thermsensor import W1ThermSensor

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)
canales=[AnalogIn(mcp, MCP.P0),AnalogIn(mcp, MCP.P1),AnalogIn(mcp, MCP.P2),AnalogIn(mcp, MCP.P3),AnalogIn(mcp, MCP.P4),AnalogIn(mcp, MCP.P5),
                 AnalogIn(mcp, MCP.P6),AnalogIn(mcp, MCP.P7)]
termo=[W1ThermSensor(sensor_id="3c01b556bfaa")]
semillas={0:['sin uso', 0, 0],1:['zanahoria', 20, 70], 2:['papa', 22, 70]}


class bandeja():

    def __init__(self, canal=0, semilla=0, estado=0):
        self.sensor_t = termo[canal]
        self.canal = canal
        self.estado= estado 
        self.sensor_h=canales[canal]
        self.semilla=semillas[semilla]
    
    
    def humedad(self):
       # print(self.sensor_h.voltage)
        humedad=((self.sensor_h.voltage)*(-30.3030))+100
        return humedad
    
    def temperatura(self):
        #print(self.sensor_t.get_temperature())
        
        return self.sensor_t.get_temperature()


class PI_simple: 

    def __init__(self, P=0.1,I=0.1,current_time=None):
       
       
        self.sample_time = 0.00
        
        self.Kp = P
        self.Ki = I
        self.current_time = current_time if current_time is not None else time.time()
        self.last_time = self.current_time
        self.clear()

    def prueba(selft):

      print("holi")
    
    def luz(self):

      if True:

        print("hola")
      
      else:

        print(0)

    def clear(self):

        self.setPoint = 0.0

        self.P = 0.0

        self.I = 0.0
    
        self.last_error = 0.0


        self.output = 0.0
          
    def update(self, feedback_value, setpoint ,current_time=None):
      
      error=setpoint-feedback_value
      self.current_time = current_time if current_time is not None else time.time()
      delta_time = self.current_time - self.last_time
      delta_error = error - self.last_error

       

      if (delta_time >= self.sample_time):
            self.P = self.Kp * error
            self.I= self.Ki*(delta_error * delta_time)
            self.output= self.P+self.I

      if(self.output < -0.3):

        self.output=-1
        
      elif (self.output > 0.3 and self.output < 0.3 ):

        self.output=0

      else:
        self.output=1

       # print(delta_time, delta_error, error)
      print(self.output)
      return self.output
    #error, self.I, delta_error, delta_time

class semilla():

    def __init__(self, nombre, temperatura, humedad): 
        self.nombre = nombre
        self.temperatura= temperatura
        self.humedad= humedad