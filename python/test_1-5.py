import lcm
import numpy as np
from lcmtypes import mbot_motor_command_t, timestamp_t
import time

lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")

DRIVE_LENGTH = 2
STOP_LENGTH = 0.2
ROTATE_LENGTH = 1

def current_utime(): return int(time.time() * 1e6)

# Drive forward
# for v in [0.25, 0.5, 1]:
# v = 1
# sleep = 2 if v != 1 else 1
# drive = mbot_motor_command_t()
# drive.utime = current_utime()
# drive.trans_v = v
# drive.angular_v = 0.0

# drive_time = timestamp_t()
# drive_time.utime = drive.utime

# lc.publish("MBOT_TIMESYNC", drive_time.encode())
# lc.publish("MBOT_MOTOR_COMMAND", drive.encode())
# time.sleep(sleep)

# # Stop
# stop = mbot_motor_command_t()
# stop.utime = current_utime()
# stop.trans_v = 0.0
# stop.angular_v = 0.0

# stop_time = timestamp_t()
# stop_time.utime = stop.utime
# lc.publish("MBOT_TIMESYNC", stop_time.encode())
# lc.publish("MBOT_MOTOR_COMMAND", stop.encode())
# time.sleep(1)


wl = [np.pi/8, np.pi/2, np.pi]
w = wl[2]
sleep = 2
drive = mbot_motor_command_t()
drive.utime = current_utime()
drive.trans_v = 0.0
drive.angular_v = w

drive_time = timestamp_t()
drive_time.utime = drive.utime

lc.publish("MBOT_TIMESYNC", drive_time.encode())
lc.publish("MBOT_MOTOR_COMMAND", drive.encode())
time.sleep(sleep)

# Stop
stop = mbot_motor_command_t()
stop.utime = current_utime()
stop.trans_v = 0.0
stop.angular_v = 0.0

stop_time = timestamp_t()
stop_time.utime = stop.utime
lc.publish("MBOT_TIMESYNC", stop_time.encode())
lc.publish("MBOT_MOTOR_COMMAND", stop.encode())
time.sleep(1)
