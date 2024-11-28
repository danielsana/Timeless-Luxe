from flask import *

import pymysql

app = Flask(__name__)

@app.route('/')
def home():
     # connect to db 
    connection = pymysql.connect(host="localhost", user='root', password='', database='project-oct')

    # fetch luxury watches 
    sql1 = 'select * from products where product_category = "Luxury Watches"'
    cursor = connection.cursor()
    cursor.execute(sql1)
    luxury = cursor.fetchall()

    # fetch  casual watches
    sql1 = 'select * from products where product_category = "Casual Watches"'
    cursor = connection.cursor()
    cursor.execute(sql1)
    casual = cursor.fetchall()

    # fetch  casual watches
    sql1 = 'select * from products where product_category = "Sports Watches"'
    cursor = connection.cursor()
    cursor.execute(sql1)
    sports = cursor.fetchall()

    return render_template('home.html', luxury=luxury, casual=casual, sports=sports)

@app.route('/upload',methods=['POST','GET'])
def upload():
    # Below if works when the Form in upload.html is Submitted/Sent
    if request.method == 'POST':
         # Below receives all variables sent/submitted from the Form
        product_name = request.form['product_name']
        product_desc = request.form['product_desc']
        product_cost = request.form['product_cost']
        product_category = request.form['product_category']
        product_image_name = request.files['product_image_name']
        product_image_name.save('static/images/' + product_image_name.filename) 
        # Saves the image File in images folder, in static Folder.

        # connect to db
        connection = pymysql.connect(host="localhost", user='root', password='', database='project-oct')

        cursor =connection.cursor()

        sql ='insert into products (product_name,product_desc,product_cost,product_category,product_image_name) values (%s,%s,%s,%s,%s)'
        try:
            cursor.execute(sql,(product_name,product_desc,product_cost,product_category,product_image_name.filename))
            connection.commit()
            return render_template('upload.html', message="product added success")
        except:
            connection.rollback()
            return render_template('upload.html', message="Failed to add the product")
    else:
        return render_template('upload.html')

app.run(debug=True)