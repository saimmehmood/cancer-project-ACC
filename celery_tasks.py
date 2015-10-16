#from celery import Celery
#from subprocess import call
import os

#app = Celery('tasks', backend='amqp', broker='amqp://')

#call(["ls", "-l"])

# Remember to give the complete path to the folders
def run_CellProfiler(inputFolder, outputFolder, pipeline):
	cellProfiler = 'python ~/CellProfiler/CellProfiler.py'
	os.system(cellProfiler + ' -c -i ' + inputFolder + ' -o ' + outputFolder + ' -p ' + pipeline)




run_CellProfiler('~/TranslocationData', '~/output', '~/simpletransproject.cppipe')
