#!/bin/sh

# Set touchpad
xinput set-prop "ELAN0504:00 04F3:3091 Touchpad" "libinput Tapping Enabled" 1

# Language
setxkbmap latam

# Transparency
picom &

# Batt icon
cbatticon -u 5 &

# Volume icon
volumeicon &

# Wifi icon
nm-applet &

# Mount usb
udiskie -t & 

# Wallpaper
nitrogen --restore &
