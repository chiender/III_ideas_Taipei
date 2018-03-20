from sht1x.Sht1x import Sht1x as SHT1x
import mysql.connector
import time
from datetime import datetime

dataPin=11
clkPin=7
sht1x=SHT1x(dataPin,clkPin, SHT1x.GPIO_BOARD)
temperature=sht1x.read_temperature_C()
humidity=sht1x.read_humidity()
dewPoint=sht1x.calculate_dew_point(temperature,humidity)
print("Temperature:{} Humidity:{} Dew Point:{}".format(temperature,humidity,dewPoint))

      
db=mysql.connector.connect(host="localhost",user="root",passwd="aidsabcgod",db="test")
curs=db.cursor()
#db.close()
try:
        now=time.time()
        now2=datetime.now()
        #[ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)		#Get the temperature and Humidity from the DHT sensor
        #print time.ctime(now)," temp =", temp, "C\thumidity =", hum,"%" 	
        #print now2," temp =", temp, "C\thumidity =", hum,"%" 
        t = str(temperature)
        h = str(humidity)
        
        #setRGB(0,128,64)
        #setRGB(0,255,0)
        #setText("Temp:" + t + "C      " + "Humidity :" + h + "%")

        dht_insert="insert into temp(date, temp, hum) values (%s, %s, %s)"
        #dhtrecord=(time.ctime(now),t,h)
        now3=str(now2.year) + "-" + str(now2.month)+"-"+str(now2.day)+" "+str(now2.hour)+":"+str(now2.minute)+":"+str(now2.second)
        
        dhtrecord=(now3,t,h)
        curs.execute(dht_insert, dhtrecord)
        db.commit()
        
except (IOError,TypeError) as e:
        print "Error"
        #curs.close()
        #db.close()
except KeyboardInterrupt:
        print "KeyboardInterrupt"
        curs.close()
        db.close()
