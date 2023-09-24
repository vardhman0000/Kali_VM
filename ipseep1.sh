#!/bin/bash

if [ "$1" == "" ];
then
    echo "You Forgot to type IP Address"
    echo "Syntax : ./ipweep.sh 192.168.33"
else
    for ip in $(seq 1 254); do
        ping -c1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":"
    done
fi
