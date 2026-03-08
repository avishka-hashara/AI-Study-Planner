from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Configure the PostgreSQL database connection
# Make sure to replace 'your_password' with your actual PostgreSQL password!
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/study_planner_db'
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)