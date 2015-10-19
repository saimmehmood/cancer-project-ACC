from celery import Celery
#from subprocess import call
import os
import urllib
import bucket_management as bm

app = Celery('celery_tasks', backend='amqp', broker='amqp://')

#call(["ls", "-l"])

# Remember to give the complete path to the folders
@app.task(name='celery_tasks.run_CellProfiler', bind=True)
def run_CellProfiler(self, inputFolder, outputFolder, pipeline):
#def run_CellProfiler():
	#url = 'http://smog.uppmax.uu.se:8080/swift/v1/jonas-cp-bucket/'
	#fileinput = urllib.urlopen(url)
	#for item in fileinput:
		#urllib.urlretrieve(url + item)
	#html = fileinput.read()
	#print html
	os.system('mkdir input_folder')
	os.chdir('input_folder')
	os.system('swift download jonas-cp-bucket')
	os.chdir('..')
	cellProfiler = 'python ~/CellProfiler/CellProfiler.py'
	os.system(cellProfiler + ' -c -i ' + 'input_folder' + ' -o ' + outputFolder + ' -p ' + pipeline)
	os.system('ls -l')
	return 0

@app.task(name='celery_tasks.dummy_function', bind=True)
def dummy_function(self):
	print "Hello!"
	return 0

#run_CellProfiler('~/TranslocationData', '~/output', '~/simpletransproject.cppipe')
#run_CellProfiler()
