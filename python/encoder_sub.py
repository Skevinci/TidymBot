import sys

import lcm

from lcmtypes import mbot_encoder_t

lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=1")


def enc_handler(channel, data):
    msg = mbot_encoder_t.decode(data)
    print("got encoder message: %d %d" % (msg.leftticks, msg.rightticks))


sub = lc.subscribe("MBOT_ENCODERS", enc_handler)

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    print("lcm exit!")
    sys.exit()
