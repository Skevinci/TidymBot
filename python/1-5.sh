cp /home/pi/mbot-controller-pico/build/src/mbot.uf2 /media/pi/RPI-RP2
sleep 2
lcm-logger logs/1 &
./shim &
./timesync &
sleep 2
python app.py
sleep 1
./kill.sh shim
./kill.sh timesync
./kill.sh lcm-logger
python3 plot_step.py logs/1
rm -f logs/1
