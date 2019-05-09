#!/bin/tcsh
echo "Start job on" `date`
echo "Running on: `uname -a`" #Condor job is running on this node

echo "System software: `cat /etc/redhat-release`" #Operating System on that node

source /cvmfs/cms.cern.ch/crab3/crab.csh
source /cvmfs/cms.cern.ch/cmsset_default.csh

xrdcp root://cmseos.fnal.gov//store/user/xiaowang/condor/CMSSW.tgz ./CMSSW.tgz

tar -xvf CMSSW.tgz
echo 'untar has been done'
#rm CMSSW.tgz
cd CMSSW_10_3_3/src/

eval `scramv1 runtime -csh`

echo 'compiling pwhg_main ...'
cd mcGenerator/POWHEG-BOX-V2/dijet/
make pwhg_main
echo 'compile finished.'

cd ../../WORKFOLDER/
mv INPUT powheg.input
echo 'running the pwhg_main...'
../POWHEG-BOX-V2/dijet/pwhg_main

xrdcp pwgevents.lhe  root://cmseos.fnal.gov//store/user/xiaowang/condor/POWHEG/OUTPUT
cd ${_CONDOR_SCRATCH_DIR}
rm -rf CMSSW_10_3_3

echo 'Done!'
