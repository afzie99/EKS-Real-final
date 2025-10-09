from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Mini Calculator API is running"})

@app.route('/add')
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"operation": "add", "result": a + b})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

@app.route('/subtract')
def subtract():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"operation": "subtract", "result": a - b})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

@app.route('/multiply')
def multiply():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify({"operation": "multiply", "result": a * b})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

@app.route('/divide')
def divide():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        if b == 0:
            return jsonify({"error": "Division by zero"}), 400
        return jsonify({"operation": "divide", "result": a / b})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
