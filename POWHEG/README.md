
## The POWHEG generator

This is the code for running standalone powheg generator at LPC. 

Run the script below first to get the POWHEG BOX v2:
```sh
/bin/sh init.sh
```

Customize the `scrip_template.csh` based on how you would like to run on the node.

An example of hadronizer built based on PYTHIA8 is in the hadronzier folder.

In case you cold compile the POWHEG smoothly in node, please check the `Makefile` in your interested process folder to make sure the compiling configs have been setup correctly. To submit the condor jobs for generating the events:

```sh
python run_powheg_condor.py
```

this script will make a script and config file for each subjobs and compact all of them into a tarball stored at EOS which is accessible by the condor node. 
