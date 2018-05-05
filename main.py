import sys
import time
from threading import Thread
from random import Random
from drive import Drive
from grab import Grab
from distance_detector import DistanceDetector
from color_detector import ColorDetector


class Main:
    drive_proc = True
    detect_boundary = True
    detecting = True
    detect_cube_found = False
    continue_driving = True

    def __init__(self, color):
        self.random = Random()
        self.drive = Drive()
        self.grab = Grab()
        self.dd = DistanceDetector()
        self.cd = ColorDetector(color)

    def turn_ninety_degrees(self):
        self.drive.turn(Drive.DIRECTION_LEFT, 88)

    def detect_outer_boundary(self):
        while self.detecting:
            while self.detect_boundary:
                detect = False
                if not self.detect_cube_found:
                    detect = self.cd.detect_boundary()
                if detect:
                    break
                time.sleep(0.01)
            self.continue_driving = False
            self.drive.stop()
            time.sleep(1)
            self.drive.reverse(70)
            time.sleep(2)
            self.drive.turn(Drive.DIRECTION_LEFT, self.random.randint(60, 180))
            self.drive.drive_continuous()
            self.continue_driving = True

    # def drive_process(self):
    #     self.drive.drive_forward(275)
    #     time.sleep(1)
    #     self.turn_ninety_degrees()
    #     for i in range(250, 0, -20):
    #         if not self.drive_proc:
    #             break
    #         for j in range(1, 4):
    #             time.sleep(0.5)
    #             if not self.drive_proc:
    #                 break
    #             self.drive.drive_forward(i)
    #             time.sleep(1)
    #             if not self.drive_proc:
    #                 break
    #             self.turn_ninety_degrees()
    #     self.drive.stop()

    def proc(self):
        self.drive.drive_continuous()
        self.dd.detect()
        self.detect_cube_found = True
        self.drive.stop()
        time.sleep(0.5)
        self.grab.lift()
        time.sleep(1)
        detected = False
        attempts = 0
        max_attempts = 6
        while not detected:
            detected = self.cd.detect()
            if not self.continue_driving:
                time.sleep(0.02)
                detected = False
            if detected:
                break
            else:
                attempts += 1
                if attempts >= max_attempts:
                    self.drive.reverse(20)
                    self.grab.sink()
                    time.sleep(2)
                    self.drive.turn(Drive.DIRECTION_RIGHT, 80)
                    self.detect_cube_found = False
                    return
            self.drive.turn(Drive.DIRECTION_LEFT, 5)
        time.sleep(0.5)
        self.drive.reverse(5)
        time.sleep(1)
        self.grab.sink()
        time.sleep(1)
        self.drive.turn(Drive.DIRECTION_RIGHT, attempts * 5)
        time.sleep(1)
        self.drive.drive_continuous()
        self.continue_driving = False
        self.detect_cube_found = False


if __name__ == '__main__':
    color = sys.argv[1]
    m = Main(color)
    try:
        m.drive.turn(Drive.DIRECTION_LEFT, 40)
        m.drive.drive_continuous()
        t_detect = Thread(target=m.detect_outer_boundary)
        t_detect.start()
        while True:
            if m.continue_driving:
                m.proc()
            time.sleep(0.05)
    except KeyboardInterrupt:
        m.drive.stop()
        sys.exit()
