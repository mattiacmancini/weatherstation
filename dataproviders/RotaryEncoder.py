from machine import Pin, Timer
from math import pi


class WindSpeedEncoder:

    _ONBOARD_LED = Pin(25, Pin.OUT)
    _ANEMOMETER_RADIUS = 125  # mm
    _ENCODER_NOTCHES = 18

    def __init__(self, phototransistor_pin, emitter_pin, time_interval=1000):
        self.ir_receiver = Pin(phototransistor_pin, Pin.IN)
        self.ir_emitter = Pin(emitter_pin, Pin.OUT)
        self.time_interval = time_interval
        self.true_count = 0
        self.timer = Timer()

    @property
    def wind_speed(self):
        base_arc = 360 / self._ENCODER_NOTCHES * pi / 180 * self._ANEMOMETER_RADIUS
        windspeed = self.true_count * base_arc / 1000  # m/s
        return windspeed

    def ir_reader(self, pin):
        if pin.value() == 1:
            self.true_count += 1
            self._ONBOARD_LED.value(1)

    def timer_callback(self, timer):
        print("TRUE count in one second:", self.true_count)
        print("WIND SPEED:", self.wind_speed, " m/s")
        self.true_count = 0  # Reset the count
        self._ONBOARD_LED.value(0)

    def run(self):
        self.ir_emitter.value(1)  # Set emitter pin ON
        self.ir_receiver.irq(self.ir_reader, Pin.IRQ_FALLING | Pin.IRQ_RISING)
        self.timer.init(period=self.time_interval, mode=Timer.PERIODIC, callback=self.timer_callback)
