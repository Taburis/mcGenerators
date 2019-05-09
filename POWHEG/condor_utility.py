
from optparse import OptionParser

def preparePOWHEGInputCard(parlist):
	parser = OptionParser();
	parser.add_option('-n', '--number', dest = 'evtN',      default = '5000',   help = '# of events to generate')
	parser.add_option('-i', '--input',  dest = 'inputCard', default = '',       help = 'POWHEG input card name')
	parser.add_option('-s', '--seed',   dest = 'seed',      default = '314159', help = 'random seed')
	parser.add_option('-f', '--folder', dest = 'folder',    default = 'testrun',help = 'the folder to dump the input card')
	parser.add_option('-j', '--job', dest = 'job',    default = '1',help = 'nth job')
	(args, opt) = parser.parse_args(parlist)
	if args.inputCard == '' : 
		print 'ERROR: no input card specified, ABORT!'
		return
	target = []
	target.append('NEVENTS')	
	target.append('SEED')	
	content = []
	content.append(args.evtN)	
	content.append(args.seed)	
	subText(args.inputCard, args.folder+'/powheg_'+args.job+'.input', target, content)
	

def subText(inf, outf, target, content):
	if len(content) != len(target): 
		print 'target and content does not match!'
		return
	ff = open(inf, 'r')
	lines = ff.readlines()
	of = open(outf, 'w+')
	newlines = []
	for line in lines:
		newline = line
		for i in xrange(0, len(target)):
			newline = newline.replace(target[i], content[i], 1)
		newlines.append(newline)
	of.writelines(newlines)	
	
'''
if __name__ == '__main__' :
	workfolder = 'testrun'
	run_name = 'test'
	jnumber = 1
	script_name = 'script_'+run_name+'_'+str(jnumber)+'.csh'
	subText('scrip_template.csh', workfolder+'/'+script_name, ['WORKFOLDER'], [workfolder])
	subText('condor_cfg_template.cfg', workfolder+'/condor_cfg_'+run_name+'_'+str(jnumber)+'.cfg', ['EXE.sh'], [script_name])
	preparePOWHEGInputCard(['-n', '1000', '-f', workfolder,'-i', 'dijet_NNPDF31nnlo_5TeV.input', '-s', '325652'])
'''
