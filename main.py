from dataproviders.RotaryEncoder import WindSpeedEncoder

# Create an instance of the RotaryEncoder class
encoder = WindSpeedEncoder(1, 0)  # IR_receiver PIN, IR_emitter Pin, optional time interval (default=1000ms)

# Start the encoder
encoder.run()

# Main loop (to keep the program running)
while True:
    pass

# def read_phototransistor():
#     period = 1000
#     pulse_count = 0
#     while ticks_ms()
#     return ir_ptrans.value()
#
#
# while True:
#     ir_led(1)
#     state = read_phototransistor()
#     if state == 1:
#         print("Phototransistor is ON")
#         led.value(1)
#     else:
#         print("Phototransistor is OFF")
#         led.value(0)

# import time
# ONBOARD_LED = Pin(25, Pin.OUT)
# sensor = TemperatureReader()
# file = open("temps.txt", "w")
# rtc = RTC()
# timestamp = rtc.datetime()
# temperature = sensor.read_temperature()
# timestring = "%04d-%02d-%02d %02d:%02d:%02d" % (timestamp[0:3] + timestamp[4:7])
# file.write(timestring + "," + str(temperature) + "\n")
# file.flush()
# print(f'Temperature: {temperature} degrees C')
# ir_led(1)
# if ir_ptrans.value() == True:
#     led(1)
# else:
#     led(0)
# print(ir_ptrans.value())
# time.sleep(5)
# ir_led(0)
# if ir_ptrans.value() == True:
#     led(1)
# else:
#     led(0)
# print(ir_ptrans.value())
# time.sleep(5)
