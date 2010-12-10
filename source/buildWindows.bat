REM Configure the installer
cd pyinstaller-1.5
c:\python27\python.exe Configure.py

REM Used to generate initial makespec, but then modified to keep everything local
c:\python27\python.exe Makespec.py -K --icon=../../binaries/ASEmbed.ico --paths=../helper --out=../../binaries --onefile ../ASEmbed.py

REM Build the binaries
c:\python27\python.exe Build.py ../../binaries/ASEmbed.spec

REM Clean up
cd ../../binaries

move dist\ASEmbed.exe
rmdir /S /Q build
rmdir /S /Q dist

cd ../source
