from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://backend_p1kj_user:uoe8VqwRnlpYXkHaqne4gZdu3viSGTJI@dpg-cn7h9a2cn0vc738uud0g-a.oregon-postgres.render.com/backend_p1kj'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

from resources.models import Customers


@app.route('/register', methods=['POST'])
def register_customer():
    # Extract data from request body
    data = request.json
    name = data.get('name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    new_customer = Customers(name=name,
                             username=username,
                             email=email,
                             password=password)

    db.session.add(new_customer)
    db.session.commit()

    return {
        'message': 'Customer successfully added',
        'name': name,
        'username': username,
        'email': email,
        'password': password
    }, 200
# db.init_app(app)


with app.app_context():
    db.create_all()




