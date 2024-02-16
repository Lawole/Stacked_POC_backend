from flask import Flask, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity
# from werkzeug.security import safe_str_cmp