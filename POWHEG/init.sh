#!/bin/sh

svn checkout --username anonymous --password anonymous svn://powhegbox.mib.infn.it/trunk/POWHEG-BOX-V2

#list all the avaliable process:
svn list  --username anonymous --password anonymous svn://powhegbox.mib.infn.it/trunk/User-Processes-V2 


#download the necessary process: here we download the dijet
svn co --username anonymous --password anonymous svn://powhegbox.mib.infn.it/trunk/User-Processes-V2/dijet
