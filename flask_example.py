from flask import Flask, render_template, request, send_from_directory
from os import listdir
import sys
output_folder = sys.argv[1]
if (output_folder[-1] == '/'):
	output_folder = output_folder[:-1]
print output_folder
app = Flask(__name__, static_folder=output_folder)

def find_items(directory):
	items = listdir(directory)
	return items

@app.route('/' + output_folder + '/<path:filename>', methods=['GET', 'POST'])
def send_file(filename):
	return send_from_directory(app.static_folder, filename, as_attachment=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', directory=find_items(output_folder))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
