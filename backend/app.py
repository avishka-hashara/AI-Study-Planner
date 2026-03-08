from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Configure the PostgreSQL database connection
# Make sure to replace 'your_password' with your actual PostgreSQL password!
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:your_password@localhost/study_planner_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- DATABASE MODELS ---

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # This establishes the relationship to the Subject table
    subjects = db.relationship('Subject', backref='user', lazy=True)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    proficiency = db.Column(db.String(50), nullable=False) # e.g., Beginner, Intermediate
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# --- ROUTES ---

@app.route('/api/test', methods=['GET'])
def test_connection():
    return jsonify({"message": "Connection successful! Hello from Flask."})

@app.route('/api/add-subject', methods=['POST'])
def add_subject():
    data = request.json
    
    # For now, let's create a dummy user if one doesn't exist just to test
    user = User.query.filter_by(username="test_student").first()
    if not user:
        user = User(username="test_student", email="test@example.com")
        db.session.add(user)
        db.session.commit()

    # Create the new subject linked to our user
    new_subject = Subject(name=data['name'], proficiency=data['proficiency'], user_id=user.id)
    
    db.session.add(new_subject)
    db.session.commit()
    
    return jsonify({"message": f"Subject '{new_subject.name}' added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)