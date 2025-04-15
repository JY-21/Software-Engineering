# app.py (no changes needed)
from flask import Flask, request, jsonify
from calculator_logic import evaluate_expression

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    expr = request.args.get('expression')
    if not expr:
        return jsonify({'error': 'No expression provided'}), 400

    result = evaluate_expression(expr)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
