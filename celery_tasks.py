from celery import Celery
#from subprocess import call
import os

app = Celery('celery_tasks', backend='amqp', broker='amqp://')

#call(["ls", "-l"])

# Remember to give the complete path to the folders
@app.task(name='celery_tasks.run_CellProfiler', bind=True)
def run_CellProfiler(self, inputFolder, outputFolder, pipeline):
	cellProfiler = 'python ~/CellProfiler/CellProfiler.py'
	os.system(cellProfiler + ' -c -i ' + inputFolder + ' -o ' + outputFolder + ' -p ' + pipeline)
	return 0

#run_CellProfiler('~/TranslocationData', '~/output', '~/simpletransproject.cppipe')
