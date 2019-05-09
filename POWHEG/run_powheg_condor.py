
import condor_utility as cu
from optparse import OptionParser
import random
import os

def prepareToSubmit(workfolder, run_name, jnumber, nevt, inputcardname, seed):
	script_name = 'script_'+run_name+'_'+str(jnumber)+'.csh'
	cu.subText('scrip_template.csh', workfolder+'/'+script_name, ['WORKFOLDER', 'INPUT', 'OUTPUT'], [workfolder, 'powheg_'+str(jnumber)+'.input', run_name+'/pwgevents_'+str(jnumber)+'.lhe'])
	cu.subText('condor_cfg_template.cfg', workfolder+'/condor_'+run_name+'_'+str(jnumber)+'.cfg', ['EXE.sh','KINDEX', 'INFILE','FOLDER'], [script_name, run_name, script_name, workfolder+'/'])
	cu.preparePOWHEGInputCard(['-n', '1000', '-f', workfolder,'-i', 'dijet_NNPDF31nnlo_5TeV.input', '-s', '325652', '-j', str(jnumber)])


if __name__ == '__main__' :
	option = 'run'
	workfolder = 'testrun'
	run_name = 'test'
	nevt = 10 # number of events generated in each job
	njob = 1    # how many jobs will be submitted
	seed = 314159 # random seeds started from
	inputCard = 'dijet_NNPDF31nnlo_5TeV.input' # POWHEG input card

	if not os.path.exists('{FOLDER}'.format(FOLDER=workfolder)):
		os.system('mkdir {FOLDER}'.format(FOLDER=workfolder))
		os.system('mkdir {FOLDER}/outCondor'.format(FOLDER=workfolder))
	for i in range(0, njob):
		ss = random.randint(0, 100) 
		prepareToSubmit(workfolder, run_name, i, nevt, inputCard, seed+ss)
		cfgpath = 'condor_'+run_name+'_'+str(i)+'.cfg'
		print "condor_submit {CFG}".format(CFG=cfgpath)

	if option == 'run' : os.system("./make_tarball.csh")
	os.chdir(workfolder)
	for i in range(0, njob):
		if option == 'run':		
			os.system("condor_submit {CFG}".format(CFG=cfgpath))

