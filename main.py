from pyb import LED
import machine
from machine import Pin
import time
import utime
from sht1x import SHT1X

led = LED(2)
humid = SHT1X(gnd=Pin.board.Y5, sck=Pin.board.Y6, data=Pin.board.Y7, vcc=Pin.board.Y8)

while True:
    data = { }
    led.on()
    humid.wake_up()

    # Get local time when taking measurement
    t = utime.localtime()

    try:
        data['temperature'] = humid.temperature()
        data['humidity'] = humid.humidity(data['temperature'])
        print('temperature: {}, humidity: {}'.format(data['temperature'],
            data['humidity']))
    except SHT1X.AckException:
        print('ACK exception in temperature meter')
        errled = LED(1)
	errled.on()
        pass
    finally:
        humid.sleep()

    # Create logfile per day...
    datetimeformat = '{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}'
    isodatetime = datetimeformat.format(t[0], t[1], t[2], t[3], t[4], t[5])
    name = 'sensordata_{:04d}_{:02d}_{:02d}.log'.format(t[0], t[1], t[2])

    with open("/sd/" + name, "a") as f:
        f.write("{};{};{};\n".format(isodatetime, data['temperature'], data['humidity']))

    led.off()

    # Sleep for 300 seconds...
    time.sleep(300)


