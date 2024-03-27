from flask import Flask, render_template
import nbformat
from nbconvert import PythonExporter
import io
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for matplotlib
import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta
import os

app = Flask(__name__)

def execute_notebook(notebook_path):
    with open(notebook_path, "r") as f:
        nb = nbformat.read(f, as_version=4)

    # Execute the notebook
    exporter = PythonExporter()
    output, resources = exporter.from_notebook_node(nb)

    # Save the generated plots
    if isinstance(resources, dict) and 'outputs' in resources:
        for output_name, output_value in resources['outputs'].items():
            if output_value['output_type'] == 'display_data':
                data = output_value['data']
                if 'image/png' in data:
                    image_data = data['image/png']
                    image_path = f"{output_name}.png"
                    with open(image_path, 'wb') as f:
                        f.write(image_data)
    else:
        print("Error: Resources object is not a dictionary or does not contain 'outputs' key.")
@app.route('/')
def index():
    # Check if the plot images exist
    image_path1 = 'my_plot.png'
    image_path2 = 'my_plot1.png'
#this code checks for the plots and rearrages
    if os.path.exists(image_path1) and os.path.exists(image_path2):
        return render_template('index.html', image_path1=image_path1, image_path2=image_path2)
    else:
        return "Plot images not found. Please execute the notebook."

if __name__ == '__main__':
    notebook_path = 'check2.ipynb'

    # Check if the notebook has been modified
    notebook_modified_time = os.path.getmtime(notebook_path)
#check2
    if datetime.fromtimestamp(notebook_modified_time) > datetime.now() - timedelta(days=1):
        execute_notebook(notebook_path)

    app.run(debug=True)