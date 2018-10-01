from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import random, sys,json
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import ARRAY
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a05e08fbc2d904a43692e593a0f04431'  # to be kept secret
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///acc.db'   # to tell the program that a file named site.db exists on the relative path
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    name = db.Column(db.String(30), nullable = False)
    contact = db.Column(db.Integer(), nullable = False)
    address = db.Column(db.Text, nullable = False)
    interests = db.Column(db.Text, nullable = True)
    imei = db.Column(db.Integer(), unique = True, nullable = False, primary_key = True)
    profile_image = db.Column(db.String(200), nullable = True)
    questionanswer = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return self.name

'''
if program is run for the first time, i.e. site.db is not created yet, 
    enter create as an argument when running this app from the cmd
'''

try:
    if sys.argv[1] == 'create':
        from main import db
        db.create_all()
except:
    pass

@app.route('/register', methods = ['POST'])
def register():
    name = request.json['name']
    contact = int(request.json['contact'])
    address = request.json['address']
    interests = request.json['interests']
    imei = int(request.json['imei'])
    profile_image = request.json['profile_image']
    questionanswer = request.json['questionanswer']
    string = ''
    for item in range(len(questionanswer)):
        if string == '':
            string += questionanswer[item]["key"] + ' , ' + questionanswer[item]["value"]
        else:
            string += ' , ' + questionanswer[item]["key"] + ' , ' + questionanswer[item]["value"]
    new_user = User(name=name, contact=contact, address=address, interests=interests, imei=imei, profile_image=profile_image,questionanswer=string)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'otp': random.randint(1000, 9999)})
########################
@app.route('/checkimei', methods = ['POST'])
def check_imei():
    input_imei=int(request.json['input_imei'])
    results = User.query.filter_by(imei=input_imei).first()
    if hasattr(results, 'imei'):
        print(results.imei)
        return jsonify(True)
    else:
        return jsonify(False)
    
    
    
@app.route('/sendquestions', methods = ['POST'])
def sendquestions():
    input_imei=int(request.json['input_imei'])
    results = User.query.filter_by(imei=input_imei).first()
    if hasattr(results, 'imei'): 
        string = results.questionanswer
        split_string = string.split(',')
        queList = []
        i = 1
        while i <= 20:
            question = split_string[i-1]
            answer = split_string[i]
            queDict = {
                "Question": question,
                "Answer": answer}
            queList.append(queDict)
            i=i+2;
    
         #convert to json data
        jsonStr = json.dumps(queList)
        print(jsonStr)
        return jsonify(jsonStr)
    else:
        return jsonify(False)
    
########################3
if __name__ == '__main__':
    app.run(debug = True)
