cp /home/pi/mbot-controller-pico/build/src/mbot.uf2 /media/pi/RPI-RP2
sleep 2
./home/pi/botlab-f-23-team-6/bin/timesync &
./home/pi/botlab-f-23-team-6/bin/pico_shim &
sleep 2
./home/pi/botlab-f-23-team-6/bin/motion_controller &
./home/pi/botlab-f-23-team-6/bin/drive_square 1 &
sleep 1
./kill.sh shim
./kill.sh timesync