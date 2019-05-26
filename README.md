# pibot

Files for running a simple, yet somehow overcomplicated two-wheeled robot.

Run the controller script on boot by adding the following line to `/home/pi/.config/lxsession/LXDE-pi/autostart`

```shell
@sudo python3 /home/pi/pibot/pygame-controller.py
```

Haven't figured out why this one needs to be run with elevated privileges.
