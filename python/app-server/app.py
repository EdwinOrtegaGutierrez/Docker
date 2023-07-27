#!/usr/bin/env python3

from flask import Flask, render_template as html, url_for

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return html('index.html')

if __name__ == "__main__":
    app.run(
        host = '0.0.0.0', 
        port=8080, 
        debug=True)