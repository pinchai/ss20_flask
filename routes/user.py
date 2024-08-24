from app import app, render_template, request
from sqlalchemy import create_engine, text

try:
    engine = create_engine("mysql+mysqlconnector://root:mysql@127.0.0.1/ss20_db")
    # Test the connection
    connection = engine.connect()
except Exception as e:
    print(e)


@app.route('/user')
def user():
    module = 'user'
    return render_template('user.html', module=module)


@app.get('/userList')
def userList():
    result = connection.execute(text("SELECT * FROM user"))
    data = result.fetchall()
    connection.commit()
    for item in data:
        print(item)
    return ''


@app.post('/saveRecord')
def saveRecord():
    form = request.get_json()
    name = form.get('name')
    gender = form.get('gender')
    phone = form.get('phone')
    email = form.get('email')
    address = form.get('address')

    return f"{name} - {gender} - {phone} - {email} - {address}"

