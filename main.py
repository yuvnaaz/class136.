from flask import Flask, jsonify, request
from data import data

app = Flask(_name_)
@app.route('/') 
def index():
    return jsonify({
        'data': data,
        'message': success, 
    }),200
@app.route('/planet')
def planet():
    name  = request.args.get('name')
    planet_data = next(item for item in data if item['name']==name)
    return jsonify({
        'data':planet_data,
        'message': 'success'
    }),200
if _name_ == '_main_':
    app.run()