#!/bin/bash
# Start Left Camera Script

cd mjpg-streamer/mjpg-streamer-experimental/
sudo ./mjpg_streamer -i './input_uvc.so -d /dev/video0 -r 320x240 -f 30 -y -n' -o './output_http.so -w ./www -p 8070'
