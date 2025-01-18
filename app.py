from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

# Define database models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)

@app.route('/api/products/add', methods=['POST'])
def add_product():
    data = request.json
    return data

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
  app.run(debug=True)
