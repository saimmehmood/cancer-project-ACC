from flask import Flask, render_template, request, send_from_directory
from os import listdir
app = Flask(__name__)

def find_items(directory):
	items = listdir(directory)
	return items

@app.route('/output_folder/<path:filename>', methods=['GET', 'POST'])
def send_file(filename):
	return send_from_directory(app.static_folder, filename, as_attachment=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('hello.html', directory=find_items('output_folder'))

if __name__ == "__main__":
    app.run(debug=True)