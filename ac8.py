#!/usr/bin/env python3
import Adafruit_DHT as dht

from time import sleep
import urllib.request


def get_info():

    umidade, temperatura = dht.read_retry(dht.DHT11, 4)

    return (umidade, temperatura)


chave ='ZSNCK9M56WTWVUD0'

baseURL ='https://api.thingspeak.com/update?api_key=%s' % chave

while True:
    umidade, temp = get_info()
    print(umidade)
    print(temp)

    conn = urllib.request.urlopen(baseURL + "&field1=" + str(umidade) + "&field2=" + str(temp))

    print(conn.read())
    conn.close()
    sleep(20)


