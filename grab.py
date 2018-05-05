from ev3dev.auto import *


class Grab:
    SPD = 300 / 90
    MOTOR = OUTPUT_C

    def __init__(self):
        self.motor = Motor(Grab.MOTOR)

    def lift(self):
        self.motor.run_to_rel_pos(position_sp=Grab.SPD * 25, speed_sp=200, stop_action="brake")

    def sink(self):
        self.motor.run_to_rel_pos(position_sp=Grab.SPD * -25, speed_sp=200, stop_action="brake")


if __name__ == '__main__':
    grab = Grab()
    grab.lift()
    time.sleep(2)
    grab.sink()
