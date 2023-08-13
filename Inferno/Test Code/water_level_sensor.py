import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the water level sensor's output
water_level_sensor_pin = 18

# Set up the GPIO pin as an input
GPIO.setup(water_level_sensor_pin, GPIO.IN)

try:
    print("Water level sensor test. Press Ctrl+C to exit.")
    
    while True:
        if GPIO.input(water_level_sensor_pin) == GPIO.HIGH:
            print("Water level is high.")
        else:
            print("Water level is low.")
        
        time.sleep(1)  # Add a delay between readings

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
