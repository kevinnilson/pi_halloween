#!/usr/bin/expect -f

spawn ssh pi@192.168.1.99

expect "assword:"
send "raspberry\r"

expect "pi@raspberrypi"
send "cd halloween\r"

expect "pi@raspberrypi"
send "python pumpkin.py\r"

expect "pi@raspberrypi"
send "exit\r"
interact

