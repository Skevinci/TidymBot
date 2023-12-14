import lcm
import numpy as np
from lcmtypes import mbot_motor_command_t, timestamp_t, odometry_t
import time

lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")

DRIVE_LENGTH = 4
STOP_LENGTH = 0.2
ROTATE_LENGTH = 1

def current_utime(): return int(time.time() * 1e6)

# drive a square
for i in range(4):
    # Drive forward
    drive = mbot_motor_command_t()
    drive.utime = current_utime()
    drive.trans_v = 0.25
    drive.angular_v = 0.0

    drive_time = timestamp_t()
    drive_time.utime = drive.utime

    lc.publish("MBOT_TIMESYNC", drive_time.encode())
    lc.publish("MBOT_MOTOR_COMMAND", drive.encode())
    time.sleep(DRIVE_LENGTH)

    # Stop
    stop = mbot_motor_command_t()
    stop.utime = current_utime()
    stop.trans_v = 0.0
    stop.angular_v = 0.0

    stop_time = timestamp_t()
    stop_time.utime = stop.utime
    lc.publish("MBOT_TIMESYNC", stop_time.encode())
    lc.publish("MBOT_MOTOR_COMMAND", stop.encode())
    time.sleep(STOP_LENGTH)

    # Rotate
    rotate = mbot_motor_command_t()
    rotate.utime = current_utime()
    rotate.trans_v = 0.0
    rotate.angular_v = np.pi / 2

    rotate_time = timestamp_t()
    rotate_time.utime = rotate.utime
    lc.publish("MBOT_TIMESYNC", rotate_time.encode())
    lc.publish("MBOT_MOTOR_COMMAND", rotate.encode())
    time.sleep(ROTATE_LENGTH)

    # Stop
    stop = mbot_motor_command_t()
    stop.utime = current_utime()
    stop.trans_v = 0.0
    stop.angular_v = 0.0

    stop_time = timestamp_t()
    stop_time.utime = stop.utime
    lc.publish("MBOT_TIMESYNC", stop_time.encode())
    lc.publish("MBOT_MOTOR_COMMAND", stop.encode())
    time.sleep(STOP_LENGTH)
