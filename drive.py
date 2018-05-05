from ev3dev.auto import *


class Drive:
    SPD = 300 / 90
    MOTOR_LEFT = OUTPUT_A
    MOTOR_RIGHT = OUTPUT_B
    DIRECTION_LEFT = 0
    DIRECTION_RIGHT = 1

    def __init__(self):
        self.m_left = Motor(Drive.MOTOR_LEFT)
        self.m_right = Motor(Drive.MOTOR_RIGHT)

    def drive_forward(self, length):
        speed = 600
        s_time = (length / int(22*(600/360))) * 1000
        self.m_left.run_timed(time_sp=s_time, speed_sp=speed, stop_action="brake")
        self.m_right.run_timed(time_sp=s_time, speed_sp=speed + 1, stop_action="brake")
        time.sleep(s_time / 1000)

    def reverse(self, length):
        speed = 360
        s_time = (length / 22) * 1000
        self.m_left.run_timed(time_sp=s_time, speed_sp=-speed, stop_action="brake")
        self.m_right.run_timed(time_sp=s_time, speed_sp=-speed, stop_action="brake")
        time.sleep(s_time / 1000)

    # direction: 0 = Left, 1 = Right
    def turn(self, direction, degrees):
        if direction == Drive.DIRECTION_LEFT:
            self.m_left.stop()
            self.m_right.run_to_rel_pos(position_sp=Drive.SPD*degrees, speed_sp=400, stop_action="brake")
        elif direction == Drive.DIRECTION_RIGHT:
            self.m_right.stop()
            self.m_left.run_to_rel_pos(position_sp=Drive.SPD*degrees, speed_sp=400, stop_action="brake")
        time.sleep(2)

    def drive_continuous(self):
        self.m_left.run_forever(speed_sp=600)
        self.m_right.run_forever(speed_sp=601)

    def stop(self):
        self.m_left.stop()
        self.m_right.stop()


if __name__ == '__main__':
    drive = Drive()
    drive.drive_forward(11)
    # time.sleep(2)
    # drive.turn(Drive.DIRECTION_LEFT, 180)
    # time.sleep(2)
    # drive.turn(Drive.DIRECTION_RIGHT, 360)
