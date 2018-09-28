from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import random, sys, base64
app = Flask(__name__)


app.config['SECRET_KEY'] = 'a05e08fbc2d904a43692e593a0f04431'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.String(30), nullable = False)
    contact = db.Column(db.Integer(), nullable = False)
    address = db.Column(db.Text, nullable = False)
    interests = db.Column(db.Text, nullable = False)
    imei = db.Column(db.Integer(), unique = True, nullable = False, primary_key = True)
    profile_image = db.Column(db.LargeBinary)
    
    def __repr__(self):
        return self.name
 #changes##############   
class questionniere(db.Model):
    questions[5] = db.Column(db.String(200), nullable = False)
    answers[5] = db.Column(db.String(20), nullable = False)
    
    def __repr__
###############3
try:
    if sys.argv[1] == 'create':
        from main import db
        db.create_all()
except:
    pass

@app.route('/register', methods = ['POST'])
def register():
    name = request.json['name']
    contact = request.json['contact']
    address = request.json['address']
    interests = request.json['interests']
    imei = int(request.json['imei'])
    profile_image = request.json['profile_image']
    profile_image = base64.decodestring(profile_image.encode())
    
    #with open(name + str(imei) + '.jpg', 'wb') as image:
    #    image.write(base64.decodebytes(profile_image))
    #with open(r'C:\Users\user\y.jpg', 'wb') as image:
     #   image.write(base64.decodebytes(profile_image))
    input()
    new_user = User(name = name, contact = contact, address = address, interests = interests, imei = imei, profile_image = image.read())
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'otp': random.randint(1000,9999)})

#changes###########

def check_imei():
    input_imei=int(request.json['input_imei'])
    if(User.query.filter_by(imei=input_imei)==input_imei):
            return jsonify(True)
        else:
            return jsonify(False)
    
def check_name():
    input_name=request.json['input_name']
    if(User.query.filter_by(imei=input_name)==input_name):
        return jsonify({User.query.filter_by(imei=input_name)})
    else:
        return jsonify({"Username not registered"})

########################3

if __name__ == '__main__':
    app.run(debug = True, port = 8000)