from flask import Flask, render_template, request
import nbformat
from nbconvert import PythonExporter
import io
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for matplotlib
import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta
import os
import subprocess  # Import subprocess module
import re

app = Flask(__name__)

# Function to execute the notebook and pass parameters
def execute_notebook(notebook_path, start_date=None, end_date=None):
    # Convert the notebook to a Python script
    exporter = PythonExporter()
    with open(notebook_path, "r") as f:
        nb = nbformat.read(f, as_version=4)
    source, meta = exporter.from_notebook_node(nb)

    # Modify the script to accept start_date and end_date
    if start_date and end_date:
        source = f"start_date = '{start_date}'\nend_date = '{end_date}'\n" + source

    # Save the modified script to a temporary file
    script_path = "temp_script.py"
    with open(script_path, "w") as f:
        f.write(source)

    # Execute the script
    try:
        subprocess.run(['python', script_path], check=True, capture_output=True, text=True) # runs the program
    except subprocess.CalledProcessError as e:
        print(f"Error executing script: {e.stderr}")
        return False

    return True

@app.route('/', methods=['GET', 'POST'])
def index():
    image_path1 = 'my_plot.png'
    image_path2 = 'my_plot1.png'

    if request.method == 'POST':
        start_date = request.form.get('startDate')
        end_date = request.form.get('endDate')

        notebook_path = 'check2.ipynb'
        success = execute_notebook(notebook_path, start_date, end_date)

        if not success:
            return "Error: Notebook execution failed."

    # Check if the plot images exist
    if os.path.exists(image_path1) and os.path.exists(image_path2):
        return render_template('index.html', image_path1=image_path1, image_path2=image_path2)
    else:
        return "Plot images not found. Please execute the notebook."

if __name__ == '__main__':
    notebook_path = 'check2.ipynb'

    # Check if the notebook has been modified
    notebook_modified_time = os.path.getmtime(notebook_path)

    if datetime.fromtimestamp(notebook_modified_time) > datetime.now() - timedelta(days=1):
        execute_notebook(notebook_path)

    app.run(debug=True)
