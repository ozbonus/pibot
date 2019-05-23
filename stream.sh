raspivid -n -ih -t 0 -rot 180 -w 640 -h 480 -fps 30 -b 1000000 -o - | nc -lkv4 5001
# raspivid -n -ih -t 0 -rot 180 -w 424 -h 240 -fps 30 -b 500000 -o - | nc -lkv4 5001
# raspivid -n -ih -t 0 -rot 180 -w 424 -h 240 -fps 30 -b 500000 -o udp://192.168.2.50:5001
