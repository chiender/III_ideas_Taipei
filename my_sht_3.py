#!/usr/bin/env python
from sht1x.Sht1x import Sht1x as SHT1x
dataPin = 11
clkPin = 7
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)
temperature = sht1x.read_temperature_C()
humidity = sht1x.read_humidity()
dewPoint = sht1x.calculate_dew_point(temperature, humidity)
print ("1->")
print("Temperature: {} Humidity: {} Dew Point: {}".format(temperature, humidity, dewPoint))
dataPin = 13
clkPin = 15
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)
temperature = sht1x.read_temperature_C()
humidity = sht1x.read_humidity()
dewPoint = sht1x.calculate_dew_point(temperature, humidity)
print ("2->")
print("Temperature: {} Humidity: {} Dew Point: {}".format(temperature, humidity, dewPoint))
dataPin = 29
clkPin = 31
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)
temperature = sht1x.read_temperature_C()
humidity = sht1x.read_humidity()
dewPoint = sht1x.calculate_dew_point(temperature, humidity)
print ("3->")
print("Temperature: {} Humidity: {} Dew Point: {}".format(temperature, humidity, dewPoint))