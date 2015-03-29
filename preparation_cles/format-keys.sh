#!/bin/bash -e

for n in $(eval "echo {${1}..${2}}")
do
  echo "Insert disk $n now"
  wait_on /dev
  ls -l /dev/disk1
  diskutil eraseDisk fat32 UT7_$n MBR disk1
  diskutil eject disk1
done

