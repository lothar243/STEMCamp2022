import lcd_i2c
from time import sleep
from base64 import b64decode

# Padding the strings

list = [1, -19, 27, 22, -15, 2, 13, 14, 33, 19, 6, 21, 23, 16, 75, 5]

lcd_i2c.lcd_init()

for i, val in enumerate(list):
    #lcd_i2c.lcd_byte(i, 0)
    lcd_i2c.lcd_byte(100 - val + 2 * i, 1)

print("Your message should be displayed right now (you may need to adjust your contrast to see it clearly")
input("Press enter to quit")
lcd_i2c.lcd_init()
