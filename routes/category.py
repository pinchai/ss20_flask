from app import app, render_template, request, IMAGE_DIR
import os
import time
from sqlalchemy import create_engine, text
from helpers import file_upload

try:
    engine = create_engine("mysql+mysqlconnector://root:mysql@127.0.0.1/ss20_db")
    # Test the connection
    connection = engine.connect()
except Exception as e:
    print(e)


@app.route('/category')
def category():
    module = 'category'
    return render_template('category.html', module=module)


@app.get('/categoryList')
def categoryList():
    result = connection.execute(text("SELECT * FROM category"))
    data = result.fetchall()
    connection.commit()
    category_list = []
    for item in data:
        category_list.append(
            {
                "id": item[0],
                "name": item[1],
                "description": item[2],
            }
        )
    return category_list


@app.post('/saveCategory')
def saveCategory():
    form = request.get_json()
    name = form.get('name')
    description = form.get('description')

    result = connection.execute(text(f"INSERT INTO `category` VALUES(null,'{name}', '{description}')"))
    connection.commit()
    return f"{result}"


@app.post('/updateCategory')
def updateCategory():
    form = request.get_json()
    id = form.get('id')
    name = form.get('name')
    description = form.get('description')
    result = connection.execute(text(f"UPDATE `category` SET NAME = '{name}',description = '{description}' WHERE id = {id}"))
    connection.commit()
    return f"{result}"


@app.post('/deleteCategory')
def deleteCategory():
    form = request.get_json()
    id = form.get('id')
    result = connection.execute(text(f"Delete From `category` WHERE id = {id}"))
    connection.commit()
    return f"Delete successfully"

