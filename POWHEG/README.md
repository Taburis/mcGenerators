
## The POWHEG generator

This is the code for running standalone powheg generator at LPC. 

Run the script below first to get the POWHEG BOX v2:
```sh
/bin/sh init.sh
```

In case you cold compile the POWHEG smoothly in node, please check the `Makefile` in your interested process folder to make sure the compiling configs have been setup correctly. To submit the condor jobs for generating the events:

```sh
python run_powheg_condor.py
```
