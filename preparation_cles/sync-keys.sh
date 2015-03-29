#!/bin/bash -e

for n in $@
do
  echo "Insert disk $n now"
  vol="/Volumes/UT7_$n"
  while ! (mount|grep "$vol "); do echo -n .; sleep 1; done; echo
  while sudo mdutil -E -d -i off "$vol" 2>&1 | grep 'try again'; do echo -n .; sleep 1; done; echo
  time rsync -rtvcO --modify-window=1 --exclude=.DS_Store --delete-excluded --delete \
    staging/ "$vol" \
    #| pv --line-mode -s $(find staging|wc -l) >/dev/null
  diskutil eject $vol
done

