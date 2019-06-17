# SHT15 Logger

Temperature and Humidity Logger using SHT15 written in Python 3 (MicroPython for
the PyBoard 1.1).

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes. See deployment for notes on
how to deploy the project on a live system.

### Prerequisites

* Sensirion SHT15 Sensor (others probably work too)
* pyboard v1.1 (other MicroPython boards should work with some adjustments)

### Wiring

| pyboard       | SHT15         |
| ------------- |---------------|
| Y5            | GND           |
| Y6            | SCK           |
| Y7            | DATA          |
| Y8            | VCC           |

I recommend to also connect VBACK (P6) to a backup battery. This makes sure that
the RTC keeps time when disconnecting the board and connecting it someplace
else.


### Installing

Copy main.py and lib/sht15.py on a SD-card and plug it into the board or
the internal flash (via USB).

The logger uses the RTC to write down when the measurement has been taken. Make
sure to set date and time correctly:

```python
from pyb import RTC
rtc = RTC()
rtc.datetime((2019, 6, 12, 3, 8, 49, 20, 0)) # y, m, d, weekday, h, m s, ms
rtc.datetime()
```

## Built With

* [MicroPython](http://micropython.org/)
* [SHT15](https://www.sparkfun.com/products/retired/13683) - SHT15 breakout board
* [upython-aq-monitor](https://github.com/ayoy/upython-aq-monitor) - sht1x.py

## License

This project is licensed under the MIT License - see the
[LICENSE](LICENSE) file for details

