import os, sys
import celery_tasks as ct
import time

'''
	Example of running this method: 'python main_program.py inputFolder outputFolder pipeline'.
	Both the folders and the file has to be in the same folder as this file in order for the 
	flask call to work properly. 
'''

def main_program():
	# Check if the number of arguments to the files is correct
	if (len(sys.argv) == 2 and str(sys.argv[1]) == '--help'):
		print "This function takes 3 arguments. Example: 'python main_program.py inputFolder outputFolder pipeline'.\nAll the folders and files has to in the same folder as this program"
		return None
	elif (len(sys.argv) != 4):
		print "Error: This method takes exactly 3 arguments (" + str(len(sys.argv) - 1) + " given). \nType 'python main_program --help' for more information. "
		return None
	# If correct, proceed with program. 
	else:
		print "Starting CellProfiler"
		new_task = ct.run_CellProfiler.delay(sys.argv[1], sys.argv[2], sys.argv[3])

		while(new_task.status != 'SUCCESS'):
			time.sleep(10)
			print "Waiting for the task to complete"

		os.system('python flask_example.py ' + sys.argv[2])


if __name__ == '__main__':
	main_program()
