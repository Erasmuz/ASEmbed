#!/bin/bash

#Configure the installer
cd pyinstaller-1.5
./Configure.py

#Used to generate initial makespec, but then modified to keep everything local
#./Makespec.py -K --paths=../helper --out=../../binaries --onefile ../ASEmbed.py

#Build the binaries
./Build.py ../../binaries/ASEmbed.spec

#Clean up
cd ../../binaries
mv dist/ASEmbed ./
rm -R build/
rm -R dist
