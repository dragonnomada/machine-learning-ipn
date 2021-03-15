import base64
from io import BytesIO

from flask import Flask
from matplotlib.figure import Figure

app = Flask(__name__)

# Conectar a la BD
# Generar todo ML
# Reportes Gráfica
# Reportes PDF
# Datos JSON
# ...

@app.route("/")
def xx():
    return "<h1>Hola</h1>"

@app.route("/reporte/2021/abril")
def hello():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"

app.run();