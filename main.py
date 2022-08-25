from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from forms import add_client_form

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
    a = 'aa'

    return render_template('clients_list.html')

@app.route('/ajouter_client')
def ajouter_client():
    form =     form = add_client_form()
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # cursor.execute('INSERT INTO brand VALUES(NULL,"KDJKSJDK","DJSDHJSD")')
    # mysql.connection.commit()
    a = 'aa'
    return render_template('client_add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=2151)