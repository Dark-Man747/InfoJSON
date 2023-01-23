from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    data = {'name': 'John', 'age': 30}
    return jsonify(data)

if __name__ == '__main__':
       app.run(debug=True,host='0.0.0.0', port=1337)
