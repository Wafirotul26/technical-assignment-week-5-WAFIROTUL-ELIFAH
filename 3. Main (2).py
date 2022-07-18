#1
#mengambil humidity.py
import dht11
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = []
    for i in range(5):
        x.append(dht11.ambil())
        time.sleep(0.2)
    
    print(x)
    plt.plot(x)
    plt.show()
    

#mengulangi proses
while True:
    #mempersingkat penulisan
    hm = dht11.ambil()
    
    #merubah dari celcius ke fahrenheit, reamur, kelvin
    fahrenheit = (hm * 1.8) + 32
    reamur = (4 / 5) * hm
    kelvin = hm + 273
    
    #menampilkan hasil
    print('%0.1f Derajat Celcius sama dengan \n  %0.1f Derajat Fahrenheit \n  %0.1f Derajat Reamur \n  %0.1f Derajat Kelvin \n' %(hm,fahrenheit,reamur,kelvin))