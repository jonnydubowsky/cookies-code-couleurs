#!/bin/bash -e

startdir="$PWD"
cachedir="$startdir/cache"

while [ -d staging ]; do rm -rf staging ||:; done

mkdir staging
cd staging

mkdir .fseventsd
touch .Spotlight-V100 .fseventsd/no_log .metadata_never_index .Trashes

unzip -q "$cachedir/processing-2.2.1-windows32.zip"

mv processing-2.2.1 processing

cp "$startdir/defaults.txt" processing/lib
cp "$startdir/start.cmd" .

mkdir processing/settings
cp "$startdir/preferences.txt" processing/settings

mkdir -p mes_programmes/{modes,libraries,tools}

unzip -d mes_programmes/modes -q "$cachedir/PythonMode-0402.zip"

(
  cd mes_programmes/modes/PythonMode
  mv examples "Autres exemples"
  exdir="examples/Code, couleurs, cookies"
  mkdir -p "$exdir"
  cp -R "$startdir/../palette_complete" "$exdir"
  cp -R "$startdir/../créations" "$exdir"
  mv "Autres exemples" examples
)

cp -R "$startdir/../palette_complete" "mes_programmes/mon_programme"
mv mes_programmes/mon_programme/{palette_complete,mon_programme}.pyde
