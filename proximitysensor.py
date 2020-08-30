# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zxJ5H_ulf2Aj76i-rA7BvbXP5DonZG45
"""

import RPi.GPIO as GPIO
import time
import requests
request = None


try:
    for count in range (0,20):
      GPIO.setmode(GPIO.BOARD)
      PIN_TRIGGER = 7
      PIN_ECHO = 11
      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)
      GPIO.output(PIN_TRIGGER, GPIO.LOW)
      print("Waiting for sensor to settle")
      time.sleep(2)
      print("Calculating distance")
      GPIO.output(PIN_TRIGGER, GPIO.HIGH)
      time.sleep(0.00001)
      GPIO.output(PIN_TRIGGER, GPIO.LOW)
      while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
      while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()
      pulse_duration = pulse_end_time - pulse_start_time
      distance1 = round(pulse_duration * 17150, 2)
      print("Distance %d:" % (count+1),distance1,"cm")
      print("Calculating distance")
      print('Sending to ThinkSpeak')
      RequestToThingspeak = 'https://api.thingspeak.com/update?api_key=JPHGBNG94QSKQFFE&field1='
      RequestToThingspeak += str(distance1)
      request = requests.get(RequestToThingspeak)
      print('Request Sent')
      print(request.text)
      time.sleep(15)
      print(count)

finally:
      GPIO.cleanup()