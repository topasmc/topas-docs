TOPAS Version 3.1.0

All use of TOPAS is governed by the TOPAS License Agreement provided in this directory as LICENSE.txt.

This README shows how to install and run TOPAS with and without user extensions.

In case of problems, see the TOPAS Monte Carlo User Forum at:
topasmc.org

These instructions are written for single user installations.
Systems administrators performing multi-user installations may need to adapt these recipes.

These instructions assume the user has basic familiarity with the use of paths, shells and environment variables on their chosen operating system.
For users who have that familiarity, it should be obvious how to adapt these recipes to their own installations.
For others who do not have that familiarity, we suggest you first read some general tutorials for paths, shells and environment variables.

This product includes software developed by Members of the Geant4 Collaboration ( http://cern.ch/geant4 ) and GDCM ( http://gdcm.sourceforge.net )

0) Pre-Requisites:

Mac Users: Install XQuartz from: 
http://xquartz.macosforge.org

Debian Users: Install the following:
apt-get install libexpat1-dev
apt-get install libgl1-mesa-dev
apt-get install libglu1-mesa-dev
apt-get install libxt-dev
apt-get install xorg-dev
apt-get install build-essential


1) Install TOPAS:

Unpack the tar.gz file:
tar -zxvf topas_3_1_*.tar.gz
Mac: Move the result so that you have /Applications/topas
Linux: Move the result so that you have ~/topas


2) Install Data Files:
The only part of Geant4 that you need to install are the data files.
You do not need to download or build any other part of Geant4 since the necessary Geant4 libraries and header files are already included in TOPAS.
If you are simply upgrading from a previous TOPAS version that uses the same Geant4 version,
you will already have these data files and can skip this step.

Mac: Download Geant4 Data files from the command line using curl:
curl -O http://geant4.cern.ch/support/source/G4EMLOW.6.50.tar.gz
curl -O http://geant4.cern.ch/support/source/G4NDL.4.5.tar.gz
curl -O http://geant4.cern.ch/support/source/G4PhotonEvaporation.4.3.2.tar.gz
curl -O http://geant4.cern.ch/support/source/G4RadioactiveDecay.5.1.1.tar.gz
curl -O http://geant4.cern.ch/support/source/G4SAIDDATA.1.1.tar.gz
curl -O http://geant4.cern.ch/support/source/G4NEUTRONXS.1.4.tar.gz
curl -O http://geant4.cern.ch/support/source/G4PII.1.3.tar.gz
curl -O http://geant4.cern.ch/support/source/RealSurface.1.0.tar.gz
curl -O http://geant4.cern.ch/support/source/G4ABLA.3.0.tar.gz
curl -O http://geant4.cern.ch/support/source/G4ENSDFSTATE.2.1.tar.gz
curl -O http://geant4.cern.ch/support/source/G4TENDL.1.3.tar.gz

Linux: Download Geant4 Data files from the command line using wget:
wget http://geant4.cern.ch/support/source/G4EMLOW.6.50.tar.gz
wget http://geant4.cern.ch/support/source/G4NDL.4.5.tar.gz
wget http://geant4.cern.ch/support/source/G4PhotonEvaporation.4.3.2.tar.gz
wget http://geant4.cern.ch/support/source/G4RadioactiveDecay.5.1.1.tar.gz
wget http://geant4.cern.ch/support/source/G4SAIDDATA.1.1.tar.gz
wget http://geant4.cern.ch/support/source/G4NEUTRONXS.1.4.tar.gz
wget http://geant4.cern.ch/support/source/G4PII.1.3.tar.gz
wget http://geant4.cern.ch/support/source/RealSurface.1.0.tar.gz
wget http://geant4.cern.ch/support/source/G4ABLA.3.0.tar.gz
wget http://geant4.cern.ch/support/source/G4ENSDFSTATE.2.1.tar.gz
wget http://geant4.cern.ch/support/source/G4TENDL.1.3.tar.gz

Mac: Unpack and move to:
/Applications/G4Data/G4EMLOW6.50
/Applications/G4Data/G4NDL4.5
/Applications/G4Data/PhotonEvaporation4.3.2
/Applications/G4Data/RadioactiveDecay5.1.1
/Applications/G4Data/G4SAIDDATA1.1
/Applications/G4Data/G4NEUTRONXS1.4
/Applications/G4Data/G4PII1.3
/Applications/G4Data/RealSurface1.0
/Applications/G4Data/G4ABLA3.0
/Applications/G4Data/G4ENSDFSTATE2.1
/Applications/G4Data/G4TENDL1.3

Linux: Unpack and move to:
~/G4Data/G4EMLOW6.50
~/G4Data/G4NDL4.5
~/G4Data/PhotonEvaporation4.3.2
~/G4Data/RadioactiveDecay5.1.1
~/G4Data/G4SAIDDATA1.1
~/G4Data/G4NEUTRONXS1.4
~/G4Data/G4PII1.3
~/G4Data/RealSurface1.0
~/G4Data/G4ABLA3.0
~/G4Data/G4ENSDFSTATE2.1
~/G4Data/G4TENDL1.3


3) Set up the environment:
Mac:
export G4LEDATA=/Applications/G4Data/G4EMLOW6.50
export G4NEUTRONHPDATA=/Applications/G4Data/G4NDL4.5
export G4LEVELGAMMADATA=/Applications/G4Data/PhotonEvaporation4.3.2
export G4RADIOACTIVEDATA=/Applications/G4Data/RadioactiveDecay5.1.1
export G4SAIDXSDATA=/Applications/G4Data/G4SAIDDATA1.1
export G4NEUTRONXSDATA=/Applications/G4Data/G4NEUTRONXS1.4
export G4PIIDATA=/Applications/G4Data/G4PII1.3
export G4REALSURFACEDATA=/Applications/G4Data/RealSurface1.0
export G4ABLADATA=/Applications/G4Data/G4ABLA3.0
export G4ENSDFSTATEDATA=/Applications/G4Data/G4ENSDFSTATE2.1
export G4TENDLDATA=/Applications/G4Data/G4TENDL1.3
export DYLD_LIBRARY_PATH=/Applications/topas/libexternal:$DYLD_LIBRARY_PATH

Linux Bourne shell:
export G4LEDATA=~/G4Data/G4EMLOW6.50
export G4NEUTRONHPDATA=~/G4Data/G4NDL4.5
export G4LEVELGAMMADATA=~/G4Data/PhotonEvaporation4.3.2
export G4RADIOACTIVEDATA=~/G4Data/RadioactiveDecay5.1.1
export G4SAIDXSDATA=~/G4Data/G4SAIDDATA1.1
export G4NEUTRONXSDATA=~/G4Data/G4NEUTRONXS1.4
export G4PIIDATA=~/G4Data/G4PII1.3
export G4REALSURFACEDATA=~/G4Data/RealSurface1.0
export G4ABLADATA=~/G4Data/G4ABLA3.0
export G4ENSDFSTATEDATA=~/G4Data/G4ENSDFSTATE2.1
export G4TENDLDATA=~/G4Data/G4TENDL1.3
export LD_LIBRARY_PATH=~/topas/libexternal/:$LD_LIBRARY_PATH

Linux C shell:
setenv G4LEDATA ~/G4Data/G4EMLOW6.50
setenv G4NEUTRONHPDATA ~/G4Data/G4NDL4.5
setenv G4LEVELGAMMADATA ~/G4Data/PhotonEvaporation4.3.2
setenv G4RADIOACTIVEDATA ~/G4Data/RadioactiveDecay5.1.1
setenv G4SAIDXSDATA ~/G4Data/G4SAIDDATA1.1
setenv G4NEUTRONXSDATA ~/G4Data/G4NEUTRONXS1.4
setenv G4PIIDATA ~/G4Data/G4PII1.3
setenv G4REALSURFACEDATA ~/G4Data/RealSurface1.0
setenv G4ABLADATA ~/G4Data/G4ABLA3.0
setenv G4ENSDFSTATEDATA ~/G4Data/G4ENSDFSTATE2.1
setenv G4TENDLDATA ~/G4Data/G4TENDL1.3
setenv LD_LIBRARY_PATH ~/topas/libexternal/:$LD_LIBRARY_PATH


4) Run TOPAS:
Mac: cd /Applications/topas
Linux: cd ~/topas

To run a whole set of examples:
source rundemos.csh

To run a single example:
cd to the directory that the example is in, then run topas from there, for example:
cd examples/SpecialComponents
../../topas MultiLeafCollimator_sequence.txt

To test TOPAS with DICOM:
Unzip the example DICOM directories in examples/Patient
cd examples/Patient
../../topas ViewAbdomen.txt


5) To add User Extensions:
You will need a tool called CMake (version 3.3 or newer).
Type "which cmake" to see if you already have this tool
and "cmake -version" to see what version you may have.

If you need to install CMake, install from a binary distribution at:
http://www.cmake.org/cmake/resources/software.html
Run the cmake.app
and follow the instructions in CMake's menu item: "Tools"... "How to Install for Command Line Use"

Mac Users: Install the Xcode compiler from:
https://developer.apple.com/xcode/downloads/
If you are on OSX 10.12, use Xcode 8.3.2
If you are on OSX 10.11, use Xcode 7.3.1
Users of earlier OSX versions can run the pre-built TOPAs, but can not add extensions.

Linux Users: Check that you have an appropriate version of the C++ compiler
You will need gcc >=4.8.3
To check your gcc version, gcc --version
If your gcc version is not sufficient, ask your sysadmin if there is already a newer version in some non-default installation on your system. They may be able to tell you how to switch to that version.
Otherwise, you will need to install a newer version or ask your sysadmin to do so.
Then locate the libstdc++.so file and add this directory to your LD_LIBRARY_PATH environment variable
(`export LD_LIBRARY_PATH=/path/to/gcc/lib:$LD_LIBRARY_PATH`).

Unzip the full set of Geant4 header files from topas/Geant4Headers.zip.
You should end up with a new directory: topas/Geant4Headers.
Do not use headers from any other version of Geant4 as they could appear to run OK but give wrong results!

Place your extra TOPAS code into a directory that is NOT inside of the topas directory.
For example, you might have TOPAS in:
/Applications/topas
and the extensions in:
/Applications/topas_extensions

Mac: cd /Applications/topas
Linux: cd ~/topas

cmake -DTOPAS_EXTENSIONS_DIR=/Applications/topas_extensions
make -j8

In the make statement, the value after -j, such as -j8 indicates how many threads make should use at once.
This depends on your computer's capabilties. A typical quad-core machine with hyperthreading can run efficiently with 8 threads.

Don't worry about any "Warning" messages. Only worry about messages that say "Error".

If you get any error messages, confirm that you unzipped the Geant4 header files as explained above.
Also check that you have an appropriate compiler (see notes earlier in this section).

Then set up the environment and run as in steps 3 and 4 above.

CMake caches the name of your extensions directory and watches for subsequent changes there. If you make changes to any of the extensions you were already including (such as while you are debugging your extensions), you just need to re-run
make -j8

If you add additional extensions to your extensions directory, again run the full
cmake -DTOPAS_EXTENSIONS_DIR=/Applications/topas_extensions
make -j8
