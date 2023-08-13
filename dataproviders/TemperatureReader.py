from machine import ADC
import time



class TemperatureReader:
    """
    Temperature reader from internal temperature sensor
    of the Raspberry Pi Pico
    """
    _adcpin = 4
    _sensor = ADC(_adcpin)

    def __init__(self):
        pass

    def read_temperature(cls):
        adc_value = cls._sensor.read_u16()
        volt = (3.3 / 65535) * adc_value
        temp = 27 - (volt - 0.706) / 0.001721
        return round(temp, 2)
