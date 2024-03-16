from flask import Flask, render_template

app = Flask(__name__)

std_list = [
    {
        'id': 10,
        'name': 'pinchai',
        'gender': 'male',
        'phone': '099 774 967',
        'email': 'pinchai.pc@gmail.com',
        'address': 'PhnomPenh',
    },
    {
        'id': 12,
        'name': 'sreypich',
        'gender': 'female',
        'phone': '010 774 967',
        'email': 'sreypich@gmail.com',
        'address': 'Takeo',
    }
]


@app.route('/')
@app.route('/dashboard')
def dashboard():
    module = 'dashboard'
    return render_template('dashboard.html', module=module)


@app.route('/user')
def user():
    module = 'user'
    return render_template('user.html', module=module, data=std_list)


@app.route('/add_user')
def add_user():
    module = 'user'
    return render_template('add_user.html', module=module)


@app.route('/edit_user/<int:user_id>')
def edit_user(user_id):
    module = 'user'
    user_id = user_id
    current_user = []
    for item in std_list:
        if user_id == item['id']:
            current_user = item

    return render_template('edit_user.html', module=module, data=current_user)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')


if __name__ == '__main__':
    app.run()
