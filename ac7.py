#!/usr/bin/env python3
from time import sleep
import urllib.request
import subprocess
import psutil


def get_cpu_temp():

    cur_tempcpu = "cat /sys/class/thermal/thermal_zone0/temp"

    tempcpu = subprocess.check_output(cur_tempcpu, shell=True)

    return float(tempcpu)/1000


def get_cpu_usage():
    cur_uso_cpu = psutil.cpu_percent()

    return cur_uso_cpu


chave ='ZSNCK9M56WTWVUD0'

baseURL ='https://api.thingspeak.com/update?api_key=%s' % chave

while True:
    cpu_temp = get_cpu_temp()
    print(cpu_temp)
    conn = urllib.request.urlopen(baseURL + "&field1=" + str(cpu_temp))
    print(conn.read())
    conn.close()
    sleep(20)


