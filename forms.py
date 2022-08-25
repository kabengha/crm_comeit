from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms import IntegerField, StringField, SubmitField, RadioField, DateTimeField, DateField, SelectField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp
from wtforms.fields.html5 import DateField


class add_client_form(FlaskForm):
    name = StringField(label='Nom / Prenom', validators=[Regexp(
        "^[a-zA-Z]+$"), Length(min=1, max=20)])
   
    email = StringField(label='Adresse E-mail',
                        validators=[DataRequired(), Email()])
    phone_number = StringField(label='Telephone'),
    adresse_deliv = StringField(label='Addresse'),
    city =  StringField(label='city'),
    pays =  StringField(label='pays'),
    communication = SelectField(u'Type', choices=[('Email', 'Email'), ('WhtasApp', 'WhtasApp')], validators=[
        DataRequired()]),
    submit = SubmitField(label='Ajouter un client')

 