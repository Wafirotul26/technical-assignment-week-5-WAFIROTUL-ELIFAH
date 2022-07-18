import numpy as np
import matplotlib.pyplot as plt
import Adafruit_DHT
from threading import Timer
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

x = []
def ambil():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        #print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        
        #fungsi ambil() mengembailkan hasil dalam satuan celcius    
        celcius = float("{0:0.1f}".format(temperature))
        return celcius
    
    else:
        print("Gagal mengambil data dari sensor DHT11")
ambil()