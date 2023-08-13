import time
import I2C_LCD_driver

# Create an LCD object
my_lcd_pin = I2C_LCD_driver.lcd()

try:
    while True:
        my_lcd_pin.lcd_display_string("Hello, World!", 1)  # Display on line 1
        my_lcd_pin.lcd_display_string("Raspberry Pi", 2)  # Display on line 2
        time.sleep(2)  # Display for 2 seconds
        my_lcd_pin.lcd_clear()  # Clear the display
        
except KeyboardInterrupt:
    print("Exiting...")
    my_lcd_pin.lcd_clear()  # Clear the display
