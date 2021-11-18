



import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from w1thermsensor import W1ThermSensor


class sensores():

    def __init__(self):
        self.sensor = W1ThermSensor()
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        cs = digitalio.DigitalInOut(board.D5)
        mcp = MCP.MCP3008(spi, cs) 
        self.canales=[AnalogIn(mcp, MCP.P0),AnalogIn(mcp, MCP.P1),AnalogIn(mcp, MCP.P2),AnalogIn(mcp, MCP.P3),AnalogIn(mcp, MCP.P4),AnalogIn(mcp, MCP.P5),
                 AnalogIn(mcp, MCP.P6),AnalogIn(mcp, MCP.P7)]

    def humedad(self, i):
      #  print (self.canales[i].voltage)
        return self.canales[i].voltage
    
    def temperatura(self):
        try:
        
            return self.sensor.get_temperature()
        
        except:
            print(error)
            self.temperatura
            
            