from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    module = 'master'
    return render_template('master.html', module=module)


@app.route('/dashboard')
def dashboard():
    module = 'dashboard'
    return render_template('dashboard.html', module=module)


@app.route('/user')
def user():
    module = 'user'
    return render_template('user.html', module=module)


if __name__ == '__main__':
    app.run()
