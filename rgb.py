import RPi.GPIO as GPIO
import time

class ColorfulLed(object):
    """
    a colorful led for Common-anode led.
    args:r:red_pin, g:green_pin, b:blue_pin, freq:PWM modulation frequency.

    """
    def __init__(self, r, g, b, freq = 50):
        super(ColorfulLed, self).__init__()
        self.r_pin = r
        self.g_pin = g
        self.b_pin = b
        self.freq = freq

    def gpio_init(self):
        GPIO.setmode(GPIO.BCM)
        # GPIO.setwarnings(False)
        # GPIO.cleanup()
        GPIO.setup(self.r_pin, GPIO.OUT)
        GPIO.setup(self.g_pin, GPIO.OUT)
        GPIO.setup(self.b_pin, GPIO.OUT)
        self.r = GPIO.PWM(self.r_pin, self.freq)
        self.g = GPIO.PWM(self.g_pin, self.freq)
        self.b = GPIO.PWM(self.b_pin, self.freq)
        self.r.start(0)
        self.g.start(0)
        self.b.start(0)

    def light(self, r, g, b):
        self.r_dc = 100 - r
        self.g_dc = 100 - g
        self.b_dc = 100 - b
        self.r.ChangeDutyCycle(self.r_dc)
        self.g.ChangeDutyCycle(self.g_dc)
        self.b.ChangeDutyCycle(self.b_dc)

    def turn(self, r, g, b):
        r_new_dc = 100 - r
        g_new_dc = 100 - g
        b_new_dc = 100 - b
        if r_new_dc > self.r_dc:
            r_step = 1
        else:
            r_step = -1
        if g_new_dc > self.g_dc:
            g_step = 1
        else:
            g_step = -1
        if b_new_dc > self.b_dc:
            b_step = 1
        else:
            b_step = -1
        for dc in range(self.r_dc, r_new_dc + r_step, r_step):
            self.r.ChangeDutyCycle(dc)
            print 'r:', dc
            # time.sleep(0.01)
        for dc in range(self.g_dc, g_new_dc + g_step, g_step):
            self.g.ChangeDutyCycle(dc)
            print 'g:', dc
            # time.sleep(0.01)
        for dc in range(self.b_dc, b_new_dc + b_step, b_step):
            self.b.ChangeDutyCycle(dc)
            print 'b:', dc
            # time.sleep(0.01)
        self.r_dc = r_new_dc
        self.g_dc = g_new_dc
        self.b_dc = b_new_dc

    def off(self):
        self.r.stop(100)
        self.g.stop(100)
        self.b.stop(100)
        # GPIO.output(self.r_pin, GPIO.HIGH)
        # GPIO.output(self.g_pin, GPIO.HIGH)
        # GPIO.output(self.b_pin, GPIO.HIGH)
        GPIO.cleanup()


if __name__ == '__main__':
    r = 17
    g = 27
    b = 22

    try:
        c = ColorfulLed(r, g, b, 100)
        c.gpio_init()
        # c.light(100, 100, 100)
        # raw_input("press any key to turn color.")
        # c.turn(0, 0, 0)
        # raw_input("press any key to turn color.")
        # c.turn(100, 100, 100)
        r_color = input("r:")
        g_color = input("g:")
        b_color = input("b:")
        c.light(r_color, g_color, b_color)
        raw_input("press any key to turn color.")
        r_color = input("r:")
        g_color = input("g:")
        b_color = input("b:")
        c.turn(r_color, g_color, b_color)
        raw_input("press any key to exit.")
    except KeyboardInterrupt:
        c.off()
    finally:
        c.off()
