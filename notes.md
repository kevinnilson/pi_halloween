turn on ssh
sudo raspi-config

sudo crowntab -e
@reboot python /home/pi/halloween/pumpkin.py &

@reboot python /home/pi/halloween/porch.py &