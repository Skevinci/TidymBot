cp /home/pi/mbot-controller-pico/build/src/mbot.uf2 /media/pi/RPI-RP2
sleep 2
# lcm-logger logs/1 &
# ./shim &
# ./timesync &
sleep 2
python3 app.py
