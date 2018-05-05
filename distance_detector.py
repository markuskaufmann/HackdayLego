from ev3dev.auto import *


class DistanceDetector:
    SENSOR = INPUT_2

    def __init__(self):
        self.detecting = True
        self.sensor = UltrasonicSensor(DistanceDetector.SENSOR)
        self.sensor.mode = 'US-DIST-CM'

    def detect(self):
        while self.detecting:
            distance = self.sensor.distance_centimeters
            if distance <= 5:
                break


if __name__ == '__main__':
    dd = DistanceDetector()
    dd.detect()
    print("found")
