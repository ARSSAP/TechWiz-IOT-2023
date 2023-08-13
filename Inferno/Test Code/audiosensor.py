import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO

# Hardware SPI configuration:
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# GPIO pin connected to the sensor's analog output
audio_analog_sensor_pin = 17

# Set up the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin as an output (for powering the sensor if needed)
GPIO.setup(audio_analog_sensor_pin, GPIO.OUT)
GPIO.output(audio_analog_sensor_pin, GPIO.HIGH)

try:
    print("Analog sound sensor test. Press Ctrl+C to exit.")
    time.sleep(2)  # Allow the sensor to stabilize
    
    while True:
        sensor_value = mcp.read_adc(0)  # Read analog value from channel 0
        print(f"Analog Value: {sensor_value}")
        time.sleep(0.5)  # Add a delay between readings

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
