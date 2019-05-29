# pibot

Files for running a simple, yet somehow overcomplicated two-wheeled robot.

Run the controller script on boot by adding the following line to `/home/pi/.config/lxsession/LXDE-pi/autostart`

```shell
@sudo python3 /home/pi/pibot/pygame-controller.py
```

Haven't figured out why this one needs to be run with elevated privileges.

I give my studetns an XBOX One S controller to control the robot. By default Raspbian enables "Enhanced Re-Transmission Mode" or ERTM. The contoller does not support this, however, so this feature needs to be disabled before even trying to pair the controller. Add this line to your `.bashrc` (most likely) or `.bash_profile`:

```shell
sudo bash -c 'echo 1 > /sys/module/bluetooth/parameters/disable_ertm'
```
