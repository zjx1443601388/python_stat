import os
import pdb
import time

if __name__ == "__main__":
	time.sleep(4)
	#pdb.set_trace()
	print 'my pid is %s'%(os.getpid())
	pid = os.fork()
	print pid
	if pid < 0:
		print 'Error in fork'
	elif pid == 0:
		print 'I am child process %s and my parent process is %s' %(os.getpid(),os.getpid())
	else:
		print 'I %s created a child process %s'%(os.getpid(),pid)
