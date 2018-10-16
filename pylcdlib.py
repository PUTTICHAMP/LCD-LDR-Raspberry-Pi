import pylcdlib
import time

lcd = pylcdlib.lcd(0x27,1)
#lcd.lcd_write(0x01);

for i in range(21,22):
  lcd.lcd_puts2(i,"test")
  print i
  raw_input("Press Enter to continue...")

lcd.lcd_puts("Hello",1) #display "Raspberry Pi" on line 1
lcd.lcd_puts(" World!",2) #display "Take a byte!" on line 2
while True:
    lcd.lcd_backlight(1)
    time.sleep(1.0)
    lcd.lcd_backlight(0)
    time.sleep(0.1)
   

