# This program stores data collected by a BME280 temp,humidity,pressure sensor controlled
# by a Raspberry Pi 3 via an I2C protocol. The data is written to a .csv file stored in an SD card.

from pathlib import Path
import RPi.GPIO as GPIO
import csv, time
from sensors.ada_fruit import BME280

OPATH = Path('/home','pi','pi_projects','data','temp_humidty_baro.csv')

def write_csv(data,opath=OPATH):
    try:
        with open(opath, 'a') as f:
            w = csv.writer(f)
            w.writerow(data)
        f.close()
    except Exception as e:
        print(e)
        time.sleep(5)
        write_csv(data, opath)
    return


def main(sensor):
    while True:
        temp_list = []
        pres_list = []
        humid_list = []

        t_end = time.time() + 300 
        while time.time() < t_end:
            temp_list.append(sensor.read_temperature())
            pres_list.append(sensor.read_pressure() / 100)
            humid_list.append(sensor.read_humidity())

        data = (time.time(),
                sum(temp_list) * 1.0 / len(temp_list),
                sum(pres_list) * 1.0 / len(pres_list),
                sum(humid_list) * 1.0 / len(humid_list))

        time.sleep(30)
        write_csv(data)
    return


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    print('reading sensors...')
    try:
        sensor = BME280()

    except Exception as e:
        print(e)
        exit()

    main(sensor)
