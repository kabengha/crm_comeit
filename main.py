from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

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
    a = 'aa'
    return render_template('client_add.html')


if __name__ == '__main__':
    app.run(debug=True, port=2151)