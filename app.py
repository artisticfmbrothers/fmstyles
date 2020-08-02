import requests
from flask import Flask,render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail



app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'artisticfmbrothers@gmail.com',
    MAIL_PASSWORD = '8122001fmstyles'
    )
mail = Mail(app)
'''app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/faizanproject'
db = SQLAlchemy(app)


class Contacts(db.Model):
    #sno , name,email,phon,msg,date
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(30),nullable=False)
    phon = db.Column(db.String(13),nullable=False)
    msg = db.Column(db.String(300),nullable=False)
    date = db.Column(db.String(12),nullable=True)'''

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        '''add entry'''
        name = request.form.get('name')
        email = request.form.get('email')
        phon = request.form.get('phon')
        msg = request.form.get('msg')
        '''#sno , name,email,phon,msg,date
        entry = Contacts( name=name , email=email, phon=phon, msg=msg, date=datetime.now())
        db.session.add(entry)
        db.session.commit()'''
        mail.send_message('New website message from ' + name,
                          sender = email,
                          recipients = ['artisticfmbrothers@gmail.com'],
                          body ="Email:-"+email+ "\n" +"message:-"+ msg + "\n" +"Phone no:-"+ phon
                          )
        tag = "Your is message sent!!"
    else:
        tag =""
    return render_template('contact.html',tag = tag)

@app.route('/commissionpricing')
def commissionpricing():
    return render_template('commissionpricing.html')

@app.route('/socialmedia')
def socialmedia():
    return render_template('socialmedia.html')

@app.route('/store')
def store():
    return render_template('store.html')



if __name__ == "__main__":
    app.run(debug=True)
