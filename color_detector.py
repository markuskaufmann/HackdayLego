from ev3dev.auto import *


class ColorDetector:
    COLORS = {  # 'black': 1,
              'blue': 2,
              # 'green': 3,
              'yellow': 4,
              'red': 5}
    SENSOR = INPUT_1

    def __init__(self, color):
        self.color = color
        del ColorDetector.COLORS[color]
        self.detecting = True
        self.sensor = ColorSensor(ColorDetector.SENSOR)
        self.sensor.mode = 'COL-COLOR'

    def detect(self):
        try:
            value = self.sensor.value()
            print(str(value))
            print(ColorDetector.COLORS)
            if value in ColorDetector.COLORS.values():
                return True
            return False
        except ValueError as e:
            print(e)
            return False

    def detect_boundary(self):
        try:
            color_code = 5
            colors = [color_code]
            value = self.sensor.value()
            if value in colors:
                return True
            return False
        except ValueError as e:
            print(e)
            return False


if __name__ == '__main__':
    cd = ColorDetector('blue')
    cd.detect()
