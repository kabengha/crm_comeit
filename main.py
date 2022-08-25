from asyncio.windows_events import NULL
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from forms import add_client_form
from datetime import date as date_function



app = Flask(__name__)

app.config['SECRET_KEY'] = '4C7U1364135'
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_comeitpack'


mysql = MySQL(app)


@app.route('/')
def index():
    a = 'aa'
    return render_template('index.html')






@app.route('/clients')
def clients():


    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM clients ORDER BY id DESC ')
        data_clients = cursor.fetchall()
    except:
        return redirect(url_for('erreur'))
    print(data_clients)

    return render_template('clients_list.html', data_clients=data_clients)











@app.route('/ajouter_client', methods=['GET', 'POST'])
def ajouter_client():
    form =  add_client_form()
    today = date_function.today()
    msg_err = ' '
    if request.method == 'POST' :
        try:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        except:
            return redirect(url_for('erreur'))
        name = form.name.data
        email = form.email.data
        phone_number = form.phone_number.data
        brand_name = form.phone_number.data
        adresse_deliv = form.adresse_deliv.data
        city = form.city.data
        pays = form.pays.data
        date = today.strftime("%d/%m/%Y")
        communication = form.communication.data
        try :
            cursor.exectue('SELECT * from brand WHERE brand_name = %s', [brand_name])
            get_brand = cursor.fetchone()
            
            if get_brand  is NULL :
                cursor.execute('INSERT INTO brand VALUES (NULL, %s, swsw)',(brand_name))
                cursor.connection.commit()

            cursor.execute('INSERT INTO clients VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, 0, %s)',(name, email, phone_number, adresse_deliv, city, pays, communication, date))
            cursor.connection.commit()
        except :
                msg_err = " Erreur, contacter Kaoutar Benghabrit"       
    return render_template('client_add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=2151)