from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms import IntegerField, StringField, SubmitField, RadioField, DateTimeField, DateField, SelectField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp
from wtforms.fields import DateField


class add_client_form(FlaskForm):
    name = StringField(label='Nom / Prenom', validators=[Regexp(
        "^[a-zA-Z]+$"), Length(min=1, max=20)])
   
    email = StringField(label='Adresse E-mail',
                        validators=[Email()])
    phone_number = StringField(label='Telephone')
    brand_name =  StringField(label='Nom de la marque')
    adresse_deliv = StringField(label='Addresse')
    city =  StringField(label='Ville')
    pays =  StringField(label='Pays')
    communication = SelectField(u'Type communication', choices=[('Email', 'Email'), ('WhtasApp', 'WhtasApp')], validators=[
        DataRequired()])
    submit = SubmitField(label='Ajouter un client')

 