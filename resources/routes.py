from flask import jsonify, request

from resources import db, app



# route for handling GET requests
@app.route('/api', methods=['GET'])
def get_data():
    # Example response
    return {'message': 'Hello Backend'}


# route for handling post requests




