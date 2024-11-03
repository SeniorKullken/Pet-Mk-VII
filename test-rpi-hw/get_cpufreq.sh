#!/bin/bash
# Show CPU-frequency on a Raspberry PI
# $ ./get_cpufreq.sh
echo ">> CPU Freq:" $(($(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq)/1000))MHz