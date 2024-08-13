from flask import Flask, render_template, request
app = Flask(__name__)


import routes


if __name__ == '__main__':
    app.run()
