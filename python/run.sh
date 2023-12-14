cp /home/pi/mbot-controller-pico/build/src/mbot.uf2 /media/pi/RPI-RP2
sleep 2
lcm-logger logs/3 &
./shim &
./timesync &
sleep 2
python step_test.py
sleep 1
./kill.sh shim
./kill.sh timesync
./kill.sh lcm-logger
python3 plot_step.py logs/3
rm -f logs/3