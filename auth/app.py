import random
from tempfile import template
from flask import Flask, render_template, request,flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from os import path
from flask_login import UserMixin 
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "dev-secret-key-change-later"

DB_NAME = "database.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

db = SQLAlchemy(app)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    email = db.Column(db.String(40), unique = True)
    password = db.Column(db.String(400))

if not path.exists(DB_NAME):
    with app.app_context():
        db.create_all()
        print("DB created")




images ={
    1: 'https://i.pinimg.com/736x/c0/c4/c9/c0c4c9a6aed4a15c29c6362881aba7ef.jpg',
    2:'https://i.pinimg.com/736x/78/8b/37/788b376809529fa605eaa7cbf7050f7f.jpg',
    3: 'https://i.pinimg.com/736x/72/c0/6e/72c06e850eeb396da5c991cf18aa3a2c.jpg',
    4 : 'https://i.pinimg.com/736x/71/55/a3/7155a3341ab2a092374a202b35600791.jpg',
    5 : 'https://i.pinimg.com/originals/7b/e1/ea/7be1ea583c9ae66b28efd56ea15edd25.png',
    6: 'https://i.pinimg.com/736x/b1/65/d0/b165d047203897cc1829c79591080671.jpg',
    7:'https://i.pinimg.com/736x/a1/70/3d/a1703d845cc154163fbd95b2dc50d47a.jpg' ,
    8: 'https://i.pinimg.com/736x/34/11/4c/34114cfe0a91d0f92eb8490d3e0eb68d.jpg'
}

def signup(email, password):
        
        if not User.query.filter_by(email=email).first():
            new_user = User( email = email, password = generate_password_hash(password))
            db.session.add( new_user )
            db.session.commit()
            n = random.choice(range(1,9))
            return render_template('image.html', img_uri = images[n])
        else:
            flash ('Account exists. Use login')
            return redirect('/')

def login(email, password):
     
    user =  User.query.filter_by(email=email).first()
        #check password
    if user:
        if check_password_hash(user.password , password):
            n = random.choice(range(1,9))
            return render_template('image.html', img_uri = images[n])
        else:
            flash('Wrong password')
         
    else:
        flash('Account not found. Sign up')
        return redirect('/')
     

@app.route('/', methods = ['POST', 'GET'])
def home():
    data = request.form
    email = request.form.get('email')
    password = request.form.get('password')
    action = request.form.get("action")
    if action == "login":
        return login(email , password)
    elif action == "signup":
        return signup(email, password )
    return render_template('index.html')
    # signup logic
@app.route("/image", methods=["GET", "POST"])
def logout():
    return redirect('/')



        

        


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)