from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql://backend_p1kj_user:uoe8VqwRnlpYXkHaqne4gZdu3viSGTJI@dpg-cn7h9a2cn0vc738uud0g-a.oregon-postgres.render.com/backend_p1kj')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from resources.models import Customers, Webhooks


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


# webhook URL endpoint
@app.route('/api/webhook', methods=['Post'])
def handle_webhook():
    payload = request.get_json()
    resources = payload.get('resources')
    eventName = payload.get('eventName')
    flowID = payload.get('flowID')
    timestamp = payload.get('timestamp')

    new_webhook = Webhooks(resources=resources,
                           eventName=eventName,
                           flowID=flowID,
                           timestamp=timestamp)

    print(new_webhook.resources)
    print(new_webhook.eventName)
    print(new_webhook.flowID)
    print(new_webhook.timestamp)


    return {'message': 'Webhooks received'}, 201


with app.app_context():
    db.create_all()
