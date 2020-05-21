from flask import Flask
from flask import render_template
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    dir = 'C:\\Users\\kate\\Downloads'
    films = os.listdir(dir)
    map = {}
    for film in films:
        film_path = os.path.join(dir, film)
        size = os.path.getsize(film_path)/1024.0
        map.update({film: size})
    return render_template("index.html", films=map)


app.run(debug=True)
