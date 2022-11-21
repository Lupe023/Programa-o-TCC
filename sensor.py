from machine import Pin
from time import sleep

red = Pin(16, Pin.OUT)
green = Pin(17, Pin.OUT)
infra = Pin(8, Pin.IN)
ledmotor = Pin(6, Pin.OUT)
motor = Pin(0, Pin.OUT)
IN1 = Pin(3, Pin.OUT)
IN2 = Pin(2, Pin.OUT)
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(5, Pin.OUT)

red.value(0)
green.value(1)
ledmotor.value(0)
contador = 0

def interrupcao(Pin):
  global dectectaPulso
  detectaPulso = True 

 
while True:
  
  if (infra.value() == 0):
      green.value(0)
      red.value(1)
      print("gato usando a caixa")
      sleep(5)
      ledmotor.value(1)
      detectaPulso = False
      
  elif (ledmotor.value() == 1):
        IN1.low()  #spin forward
        IN2.high()
        IN3.high()  #spin forward
        IN4.low()
        sleep(5)
        
        IN1.low()  #stop
        IN2.low()
        IN3.low()  #stop
        IN4.low()
        sleep(2)
        
        IN1.high()  #spin backward
        IN2.low()
        IN3.low()  #spin backward
        IN4.high()
        sleep(5)

        IN1.low()  #stop
        IN2.low()
        IN3.low()  #stop
        IN4.low()
        ledmotor.value(0)
        red.value(0)
        green.value(1)
        contador=contador+1
        
      
infra.irq(trigger=Pin.IRQ_FALLING, handler=infra_handler)