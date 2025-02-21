from flask import Flask, request, jsonify
from math_ops.add import calculate as add
from math_ops.sub import calculate as subtract
from math_ops.mul import calculate as multiply
from math_ops.div import calculate as divide

app = Flask(__name__)

operations = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

@app.route('/calc', methods=['POST'])
def handle_calculation():
    try:
        data = request.get_json()
        op = data['operation']
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        
        result = operations[op](num1, num2)
        return jsonify({
            'operation': op,
            'result': result
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)