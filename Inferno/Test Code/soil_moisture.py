import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the soil moisture sensor's analog output
sensor_sensor_DH = 18

# Set up the GPIO pin as an input
GPIO.setup(sensor_sensor_DH, GPIO.IN)

try:
    while True:
        # Read the moisture level from the sensor (0 = dry, 1 = wet)
        moisture_level = GPIO.input(sensor_sensor_DH)
        
        if moisture_level == GPIO.LOW:
            print("Soil is dry.")
        else:
            print("Soil is wet.")
        
        time.sleep(2)  # Delay between readings

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
