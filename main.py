import bcrypt
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message="Hello, World!")

# password hashing
@app.route('/hash', methods=['POST'])
def hash_password():
    password = request.json.get('password')
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return jsonify({"hashed_password": hashed_password.decode('utf-8')})

@app.route('/verify', methods=['POST'])
def verify_password():
    password = request.json.get('password')
    hashed_password = request.json.get('hashed_password')
    is_verified = bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    return jsonify({"verified": is_verified})






if __name__ == '__main__':
    app.run(debug=True)