from ev3dev.auto import *


class ColorDetector:
    COLORS = {'black': 1,
              'blue': 2,
              'green': 3,
              'yellow': 4,
              'red': 5,
              'white': 6,
              'brown': 7}
    SENSOR = INPUT_1

    def __init__(self):
        self.detecting = True
        self.sensor = ColorSensor(ColorDetector.SENSOR)
        self.sensor.mode = 'COL-COLOR'

    def detect(self, color):
        color_code = ColorDetector.COLORS[color]
        colors = [color_code]
        value = self.sensor.value()
        while self.detecting:
            print(str(value))


if __name__ == '__main__':
    cd = ColorDetector()
    cd.detect('red')
