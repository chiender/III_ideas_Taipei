#!/usr/bin/env python
from sht1x.Sht1x import Sht1x as SHT1x
dataPin = 11 # PIN 11; GPIO17
clkPin = 7   # PIN 7; GPIO04
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)
temperature = sht1x.read_temperature_C()
humidity = sht1x.read_humidity()
dewPoint = sht1x.calculate_dew_point(temperature, humidity)
print("Temperature: {} Humidity: {} Dew Point: {}".format(temperature, humidity, dewPoint))
