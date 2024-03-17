# from flask import Flask, render_template
# import nbformat
# from nbconvert import PythonExporter
# import io
# import base64
# import matplotlib
# matplotlib.use('Agg')  # Use the 'Agg' backend for matplotlib
# import matplotlib.pyplot as plt

# app = Flask(__name__)

# def render_notebook(notebook_path):
#     with open(notebook_path, "r") as f:
#         nb = nbformat.read(f, as_version=4)

#     # Execute the notebook
#     exporter = PythonExporter()
#     (output, _) = exporter.from_notebook_node(nb)

#     # Capture the output of the executed notebook
#     output_stream = io.StringIO()
#     output_stream.write(output)
#     output_stream.seek(0)

#     # Save the plot as an image and read the image data
#     image_buf = io.BytesIO()
#     plt.savefig(image_buf, format='png')
#     image_buf.seek(0)
#     image_data = image_buf.getvalue()

#     return image_data

# @app.route('/')
# def index():
#     # Render the notebook and get the plot image data
#     image_data = render_notebook("check2.ipynb")

#     # Encode the image data as a base64 string
#     encoded_image = base64.b64encode(image_data).decode()

#     return render_template("index.html", plot_image=encoded_image)

# if __name__ == '__main__':
#     app.run(debug=True)

##UPDATE 1 
# from flask import Flask, render_template
# import nbformat
# from nbconvert import PythonExporter
# import io
# import base64
# import matplotlib
# matplotlib.use('Agg')  # Use the 'Agg' backend for matplotlib
# import matplotlib.pyplot as plt
# import time

# app = Flask(__name__)

# def execute_notebook(notebook_path):
#     with open(notebook_path, "r") as f:
#         nb = nbformat.read(f, as_version=4)

#     # Execute the notebook
#     exporter = PythonExporter()
#     (output, _) = exporter.from_notebook_node(nb)
#     print("The notebook has been succesful compiled")
#     # Capture the output of the executed notebook
#     output_stream = io.StringIO()
#     output_stream.write(output)
#     output_stream.seek(0)

# def save_plots(image_path1, image_path2):
#     # Save the first plot (daily) as an image
#     image_buf = io.BytesIO()
#     plt.savefig(image_buf, format='png')
#     image_buf.seek(0)
#     with open(image_path1, 'wb') as f:
#         f.write(image_buf.getvalue())

#     # Save the second plot (weekly average) as an image
#     plt.figure()  # Create a new figure to avoid overwriting the previous plot
#     # Code to generate the weekly average plot from check2.ipynb
#     # ...
#     image_buf = io.BytesIO()
#     plt.savefig(image_buf, format='png')
#     image_buf.seek(0)
#     with open(image_path2, 'wb') as f:
#         f.write(image_buf.getvalue())

# @app.route('/')
# def index():
#     # Assuming 'my_plot.png' and 'my_plot1.png' are in the same directory as app.py
#     image_path1 = 'my_plot.png'
#     image_path2 = 'my_plot1.png'
#     return render_template('index.html', image_path1=image_path1, image_path2=image_path2)

# if __name__ == '__main__':
#     while True:
#         try:
#             execute_notebook("check2.ipynb")
#             save_plots('my_plot.png', 'my_plot1.png')
#             time.sleep(600)  # Update the plots every 10 minutes (600 seconds)
#         except Exception as e:
#             print("Error updating plots:", e)

#     app.run(debug=True)

##UPDATE 2
# from flask import Flask, render_template
# import nbformat
# from nbconvert import PythonExporter
# import io
# import base64
# import matplotlib
# matplotlib.use('Agg')  # Use the 'Agg' backend for matplotlib
# import matplotlib.pyplot as plt
# import time
# from datetime import datetime, timedelta
# import os

# app = Flask(__name__)

# def execute_notebook(notebook_path):
#     with open(notebook_path, "r") as f:
#         nb = nbformat.read(f, as_version=4)

#     # Execute the notebook
#     exporter = PythonExporter()
#     (output, _) = exporter.from_notebook_node(nb)

#     # Capture the output of the executed notebook
#     output_stream = io.StringIO()
#     output_stream.write(output)
#     output_stream.seek(0)

# def save_plots(image_path1, image_path2):
#     # Save the first plot (daily) as an image
#     image_buf = io.BytesIO()
#     plt.savefig(image_buf, format='png')
#     image_buf.seek(0)
#     with open(image_path1, 'wb') as f:
#         f.write(image_buf.getvalue())

#     # Save the second plot (weekly average) as an image
#     plt.figure()  # Create a new figure to avoid overwriting the previous plot
#     # Code to generate the weekly average plot from check2.ipynb
#     # ...
#     image_buf = io.BytesIO()
#     plt.savefig(image_buf, format='png')
#     image_buf.seek(0)
#     with open(image_path2, 'wb') as f:
#         f.write(image_buf.getvalue())

# @app.route('/')
# def index():
#     # Assuming 'my_plot.png' and 'my_plot1.png' are in the same directory as app.py
#     image_path1 = 'my_plot.png'
#     image_path2 = 'my_plot1.png'
#     return render_template('index.html', image_path1=image_path1, image_path2=image_path2)

# if __name__ == '__main__':
#     image_path1 = 'my_plot.png'
#     image_path2 = 'my_plot1.png'
#     notebook_path = 'check2.ipynb'

#     # Check if the plot images are older than 1 day or if the notebook has been modified
#     one_day_ago = datetime.now() - timedelta(days=1)
#     image1_modified_time = os.path.getmtime(image_path1) if os.path.exists(image_path1) else 0
#     image2_modified_time = os.path.getmtime(image_path2) if os.path.exists(image_path2) else 0
#     notebook_modified_time = os.path.getmtime(notebook_path)

#     if (
#         datetime.fromtimestamp(image1_modified_time) < one_day_ago or
#         datetime.fromtimestamp(image2_modified_time) < one_day_ago or
#         datetime.fromtimestamp(notebook_modified_time) > datetime.fromtimestamp(max(image1_modified_time, image2_modified_time))
#     ):
#         execute_notebook(notebook_path)
#         save_plots(image_path1, image_path2)

#     app.run(debug=True)

#UPDATE 3 
from flask import Flask, render_template
import nbformat
from nbconvert import PythonExporter
import io
import base64
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
    (output, _) = exporter.from_notebook_node(nb)

    # Capture the output of the executed notebook
    output_stream = io.StringIO()
    output_stream.write(output)
    output_stream.seek(0)

@app.route('/')
def index():
    # Assuming 'my_plot.png' and 'my_plot1.png' are in the same directory as app.py
    image_path1 = 'my_plot.png'
    image_path2 = 'my_plot1.png'
    return render_template('index.html', image_path1=image_path1, image_path2=image_path2)

if __name__ == '__main__':
    image_path1 = 'my_plot.png'
    image_path2 = 'my_plot1.png'
    notebook_path = 'check2.ipynb'

    # Check if the notebook has been modified
    notebook_modified_time = os.path.getmtime(notebook_path)

    if datetime.fromtimestamp(notebook_modified_time) > datetime.now() - timedelta(days=1):
        execute_notebook(notebook_path)

    app.run(debug=True)