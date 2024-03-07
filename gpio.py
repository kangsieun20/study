import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # setup 사용 시 보드 Physical 지정 가능

p = GPIO.PWM(11, 100)

p.start(0)
time.sleep(1)

p.ChangeDutyCycle(30)
time.sleep(1)

p.ChangeDutyCycle(60)
time.sleep(1)

p.ChangeDutyCycle(100)
time.sleep(3)

p.stop()

GPIO.cleanup()
