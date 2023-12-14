import lcm
import numpy as np
from lcmtypes import mbot_motor_command_t, timestamp_t
import time

lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")

DRIVE_LENGTH = 2
STOP_LENGTH = 0.2
ROTATE_LENGTH = 1

def current_utime(): return int(time.time() * 1e6)

# forward
v = 0.6
drive = mbot_motor_command_t()
drive.utime = current_utime()
drive.trans_v = v
drive.angular_v = 0.0

drive_time = timestamp_t()
drive_time.utime = drive.utime

lc.publish("MBOT_TIMESYNC", drive_time.encode())
lc.publish("MBOT_MOTOR_COMMAND", drive.encode())
time.sleep(3.8)

v = 0.3
drive = mbot_motor_command_t()
drive.utime = current_utime()
drive.trans_v = v
drive.angular_v = 0.0

drive_time = timestamp_t()
drive_time.utime = drive.utime

lc.publish("MBOT_TIMESYNC", drive_time.encode())
lc.publish("MBOT_MOTOR_COMMAND", drive.encode())
time.sleep(0.2)

# Stop
stop = mbot_motor_command_t()
stop.utime = current_utime()
stop.trans_v = 0.0
stop.angular_v = 0.0

stop_time = timestamp_t()
stop_time.utime = stop.utime
lc.publish("MBOT_TIMESYNC", stop_time.encode())
lc.publish("MBOT_MOTOR_COMMAND", stop.encode())
time.sleep(0.1)

v = -0.3
drive = mbot_motor_command_t()
drive.utime = current_utime()
drive.trans_v = v
drive.angular_v = 0.0

drive_time = timestamp_t()
drive_time.utime = drive.utime

lc.publish("MBOT_TIMESYNC", drive_time.encode())
lc.publish("MBOT_MOTOR_COMMAND", drive.encode())
time.sleep(0.3)

v = -0.6
drive = mbot_motor_command_t()
drive.utime = current_utime()
drive.trans_v = v
drive.angular_v = 0.0

drive_time = timestamp_t()
drive_time.utime = drive.utime

lc.publish("MBOT_TIMESYNC", drive_time.encode())
lc.publish("MBOT_MOTOR_COMMAND", drive.encode())
time.sleep(3.1)

v = -0.3
drive = mbot_motor_command_t()
drive.utime = current_utime()
drive.trans_v = v
drive.angular_v = 0.0

drive_time = timestamp_t()
drive_time.utime = drive.utime

lc.publish("MBOT_TIMESYNC", drive_time.encode())
lc.publish("MBOT_MOTOR_COMMAND", drive.encode())
time.sleep(0.2)

# Stop
stop = mbot_motor_command_t()
stop.utime = current_utime()
stop.trans_v = 0.0
stop.angular_v = 0.0

stop_time = timestamp_t()
stop_time.utime = stop.utime
lc.publish("MBOT_TIMESYNC", stop_time.encode())
lc.publish("MBOT_MOTOR_COMMAND", stop.encode())
time.sleep(0.5)
