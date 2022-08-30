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
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
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

    return render_template('clients_list.html', data_clients=data_clients)


@app.route('/marques')
def marques():
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM brand ORDER BY date_crea DESC ')
        data_brands = cursor.fetchall()
    except:
        return redirect(url_for('erreur'))
    return render_template('brands_list.html', data_brands=data_brands)














@app.route('/ajouter_client', methods=['GET', 'POST'])
def ajouter_client():
    form =  add_client_form()
    today = date_function.today()
    msg_err = ""
    message_succ = ""
    if request.method == 'POST' :
       
        name = form.name.data
        email = form.email.data
        phone_number = form.phone_number.data
        brand_name = form.brand_name.data
        adresse_deliv = form.adresse_deliv.data
        city = form.city.data
        pays = form.pays.data
        date = today.strftime("%d/%m/%Y")
        communication = form.communication.data
        avec_devis = form.devis.data
        vide = '-'
        client_id = ""
        devis_id = ""
        brand_id = ""

        try :
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            
            if brand_name != "" : 
                cursor.execute('SELECT * from brand WHERE brand_name = %s', [brand_name])
                get_brand = cursor.fetchone()
            
                if get_brand  is None   :
                    brand_id = brand_name.replace(" ", "")+str(today.year)
                    cursor.execute('INSERT INTO brand VALUES (%s, %s, %s, %s, %s, %s, %s)',[brand_id, brand_name, vide, vide, vide, vide, date])
                    cursor.connection.commit()
                else :
                    brand_id = get_brand['id']
            else :
                brand_id = '-'

            cursor.execute('INSERT INTO clients VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(name, email, phone_number, adresse_deliv, city, pays, communication, brand_id, date))
            cursor.connection.commit()
            client_id = cursor.lastrowid
        except :
            msg_err = " Erreur, contacter Kaoutar Benghabrit"       
        if avec_devis == "Oui" :
            status = "En attente"
            desc_produit_arr = []
            quantite_produit_arr = []
            for desc_produit, quantite_produit in zip(request.form.getlist('description_pr'),request.form.getlist('qte_pr')) :
                desc_produit_arr.append(desc_produit)
                quantite_produit_arr.append(quantite_produit)
        
            lengh_devis = len(desc_produit_arr)
            i = 0

            try :
                cursor.execute('INSERT INTO devis VALUES (NULL, %s, %s, %s, %s, %s)',
                            (status, client_id, brand_id, vide, date))
                mysql.connection.commit()
                devis_id = cursor.lastrowid
            except :
                 msg_err = " Erreur, contacter Kaoutar Benghabrit"    


            while i < lengh_devis :
                cursor.execute('INSERT INTO devis_produits_rel VALUES (NULL, %s, %s, %s, %s, %s, %s)',
                            (devis_id, vide, desc_produit_arr[i], quantite_produit_arr[i], vide, vide))
                mysql.connection.commit()
                i += 1
        message_succ = "Client bien ajouter"
        # return redirect(url_for('ajouter_client'))

    return render_template('client_add.html', form=form, msg_err=msg_err, message_succ=message_succ)


if __name__ == '__main__':
    app.run(debug=True, port=2151)