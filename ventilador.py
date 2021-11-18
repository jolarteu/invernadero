import board
import busio
from digitalio import Direction
i2c = busio.I2C(board.SCL, board.SDA)
from adafruit_mcp230xx.mcp23017 import MCP23017
import time
def main():
    mcp = MCP23008(i2c, address=0x22)
    pin0 = mcp.get_pin(7)
    pin0.direction = Direction.OUTPUT
    while true:
        pin0.value = True  # GPIO0 / GPIOA0 to high logic level
        time.sleep(5)
        pin0.value = False
if __name__ == '__main__':
    main()
