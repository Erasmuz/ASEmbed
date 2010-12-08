REM Configure the installer


cd pyinstaller-1.5

c:\python24\python.exe Configure.py



REM Used to generate initial makespec, but then modified to keep everything local

REM c:\python24\python.exe Makespec.py -K --paths=../helper --out=../../binaries --onefile ../ASEmbed.py



REM Build the binaries

c:\python24\python.exe Build.py ../../binaries/ASEmbed.spec



#Clean up

cd ../../binaries

move dist\ASEmbed.exe
rmdir /S /Q build

rmdir /S /Q dist
cd ../source
