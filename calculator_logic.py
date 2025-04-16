# calculator_logic.py

from asteval import Interpreter

# Create a safe math evaluator
aeval = Interpreter()

def evaluate_expression(expression: str) -> str:
    try:
        result = aeval(expression)
        if aeval.error:
            return "Error"
        return str(result)
    except Exception:
        return "Error"
