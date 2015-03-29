#!/bin/bash

while true; do
  for d in /Volumes/UT7_*
  do
    echo $d;
    rsync -rv --exclude=processing --exclude=modes $d saves
    diskutil eject $d
  done
  wait_on /Volumes
  sleep 2
done

