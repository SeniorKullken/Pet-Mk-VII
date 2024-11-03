#!/bin/bash
# Show CPU-temp on a Raspberry PI
# $ ./get_cputemp.sh
awk '{print $1/1000,"degrees C"}' /sys/class/thermal/thermal_zone0/temp