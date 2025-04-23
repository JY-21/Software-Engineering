import pytest
from calculator_logic import evaluate_expression

@pytest.mark.parametrize("expression,expected", [
    ("2+2", "4"),
    ("5*3", "15"),
    ("10/2", "5.0"),
    ("2+2*2", "6"),
    ("(2+2)*2", "8"),
    ("10-3", "7"),
    ("3.5 + 2.5", "6.0"),
    ("invalid + 5", "Error"),
    ("2/0", "Error"),
])
def test_evaluate_expression(expression, expected):
    assert evaluate_expression(expression) == expected
