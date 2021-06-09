from flask import Flask,  jsonify 
import os 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': 'Hello I am a developer my name is Husne Ozmen',
        'environment': os.environ.get('ENVIRONMENT'),
        'owner': 'husneozmen',
        'namespace': os.environ.get('NAMESPACE')
    })
@app.route('/husneozmen')
def comming_soon():
    return jsonify({
        'message': 'This is Husne Ozmens page'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
