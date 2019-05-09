#!/bin/tcsh


setenv CMSSW_BASE /uscms_data/d3/xiaowang/CMSSW_10_3_3

cd $CMSSW_BASE/../

echo $PWD

tar -zcvf $CMSSW_BASE/src/CMSSW.tgz CMSSW_10_3_3 --exclude="*.root" --exclude="*.pdf" --exclude="*.gif" --exclude=.git --exclude="*.log" --exclude="*.stdout" --exclude="*.stderr" 

cd $CMSSW_BASE/src

eosrm /store/user/xiaowang/condor/CMSSW.tgz

xrdcp $CMSSW_BASE/src/CMSSW.tgz root://cmseos.fnal.gov//store/user/xiaowang/condor/CMSSW.tgz

cd $CMSSW_BASE/src/mcGenerator

