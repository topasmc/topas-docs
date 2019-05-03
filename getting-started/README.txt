TOPAS Version 3.2.0

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
You will only need to do this part one time for each new computer.

Mac Users: Install XQuartz from: 
http://xquartz.macosforge.org
If you already had XQuartz, check that you have at least version 2.7.11
If you have just installed XQuartz, you will need to reboot for it to work.

Debian Users: Install the following:
apt install -y libexpat1-dev
apt install -y libgl1-mesa-dev
apt install -y libglu1-mesa-dev
apt install -y libxt-dev
apt install -y xorg-dev
apt install -y build-essential


1) Install TOPAS:
You will only need to do this part one time for each new TOPAS version.

Unpack the tar.gz file:
tar -zxvf topas_3_2_*.tar.gz

Mac: Move the result so that you have /Applications/topas
Linux: Move the result so that you have ~/topas


2) Install Data Files:
You may only need to do this one time for your first TOPAS version.

In most cases, when we upgrade TOPAS you do not need to upgrade these Data files.
The TOPAS release notes will tell you if you actually need to update these Data files.
(it only needs doing when we change the underlying Geant4 release inside of TOPAS).

The only part of Geant4 that you need to install are the data files.
You do not need to download or build any other part of Geant4 since the necessary
Geant4 libraries and header files are already included in TOPAS.


Download and Install Geant4 Data files into your /Applications/G4Data directory.

Mac:
You do this by issuing the following commands from a Terminal window:
mkdir /Applications/G4Data
cd /Applications/G4Data
curl -O http://geant4-data.web.cern.ch/geant4-data/datasets/G4NDL.4.5.tar.gz
curl -O http://geant4-data.web.cern.ch/geant4-data/datasets/G4EMLOW.7.7.tar.gz
curl -O http://geant4-data.web.cern.ch/geant4-data/datasets/G4PhotonEvaporation.5.3.tar.gz
curl -O http://geant4-data.web.cern.ch/geant4-data/datasets/G4RadioactiveDecay.5.3.tar.gz
curl -O http://geant4-data.web.cern.ch/geant4-data/datasets/G4SAIDDATA.2.0.tar.gz
curl -O http://geant4-data.web.cern.ch/geant4-data/datasets/G4PARTICLEXS.1.1.tar.gz
curl -O http://geant4-data.web.cern.ch/geant4-data/datasets/G4ABLA.3.1.tar.gz
curl -O http://geant4-data.web.cern.ch/geant4-data/datasets/G4INCL.1.0.tar.gz
curl -O http://geant4-data.web.cern.ch/geant4-data/datasets/G4PII.1.3.tar.gz
curl -O http://geant4-data.web.cern.ch/geant4-data/datasets/G4ENSDFSTATE.2.2.tar.gz
curl -O http://geant4-data.web.cern.ch/geant4-data/datasets/G4RealSurface.2.1.1.tar.gz
curl -O http://geant4-data.web.cern.ch/geant4-data/datasets/G4TENDL.1.3.2.tar.gz
tar -zxf G4NDL.4.5.tar.gz
tar -zxf G4EMLOW.7.7.tar.gz
tar -zxf G4PhotonEvaporation.5.3.tar.gz
tar -zxf G4RadioactiveDecay.5.3.tar.gz
tar -zxf G4SAIDDATA.2.0.tar.gz
tar -zxf G4PARTICLEXS.1.1.tar.gz
tar -zxf G4ABLA.3.1.tar.gz
tar -xzf G4INCL.1.0.tar.gz
tar -zxf G4PII.1.3.tar.gz
tar -zxf G4ENSDFSTATE.2.2.tar.gz
tar -zxf G4RealSurface.2.1.1.tar.gz
tar -zxf G4TENDL.1.3.2.tar.gz

Linux:
You do this by issuing the following commands from a Terminal window:
mkdir ~/G4Data
cd ~/G4Data
wget http://geant4-data.web.cern.ch/geant4-data/datasets/G4NDL.4.5.tar.gz
wget http://geant4-data.web.cern.ch/geant4-data/datasets/G4EMLOW.7.7.tar.gz
wget http://geant4-data.web.cern.ch/geant4-data/datasets/G4PhotonEvaporation.5.3.tar.gz
wget http://geant4-data.web.cern.ch/geant4-data/datasets/G4RadioactiveDecay.5.3.tar.gz
wget http://geant4-data.web.cern.ch/geant4-data/datasets/G4SAIDDATA.2.0.tar.gz
wget http://geant4-data.web.cern.ch/geant4-data/datasets/G4PARTICLEXS.1.1.tar.gz
wget http://geant4-data.web.cern.ch/geant4-data/datasets/G4ABLA.3.1.tar.gz
wget http://geant4-data.web.cern.ch/geant4-data/datasets/G4INCL.1.0.tar.gz
wget http://geant4-data.web.cern.ch/geant4-data/datasets/G4PII.1.3.tar.gz
wget http://geant4-data.web.cern.ch/geant4-data/datasets/G4ENSDFSTATE.2.2.tar.gz
wget http://geant4-data.web.cern.ch/geant4-data/datasets/G4RealSurface.2.1.1.tar.gz
wget http://geant4-data.web.cern.ch/geant4-data/datasets/G4TENDL.1.3.2.tar.gz
tar -zxf G4NDL.4.5.tar.gz
tar -zxf G4EMLOW.7.7.tar.gz
tar -zxf G4PhotonEvaporation.5.3.tar.gz
tar -zxf G4RadioactiveDecay.5.3.tar.gz
tar -zxf G4SAIDDATA.2.0.tar.gz
tar -zxf G4PARTICLEXS.1.1.tar.gz
tar -zxf G4ABLA.3.1.tar.gz
tar -xzf G4INCL.1.0.tar.gz
tar -zxf G4PII.1.3.tar.gz
tar -zxf G4ENSDFSTATE.2.2.tar.gz
tar -zxf G4RealSurface.2.1.1.tar.gz
tar -zxf G4TENDL.1.3.2.tar.gz


3) Set up the environment:
You will need to do this every time you open a fresh Terminal window.

You may choose to put this setup information into one of your startup files,
but we recommend you only do that if you are very comfortable with such things,
as you may accidentally affect other processes.

Mac:
export TOPAS_G4_DATA_DIR=/Applications/G4Data
export DYLD_LIBRARY_PATH=/Applications/topas/libexternal:$DYLD_LIBRARY_PATH

Linux Bourne shell:
export TOPAS_G4_DATA_DIR=~/G4Data
export LD_LIBRARY_PATH=~/topas/libexternal/:$LD_LIBRARY_PATH

Linux C shell:
setenv TOPAS_G4_DATA_DIR ~/G4Data
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

Mac Users: You must have Mac OS X 10.12 or newer.
Users of earlier OSX versions or those using the above OSX versions with earlier Xcode versions
can run the pre-built TOPAS, but can not add extensions.
Install the Xcode compiler, version 8.3.2 or newer, from:
https://developer.apple.com/xcode/downloads/

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
