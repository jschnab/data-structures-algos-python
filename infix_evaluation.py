import re

from stacks_queues import Stack


PRECEDENCE = {
    "*": 2,
    "/": 2,
    "+": 1,
    "-": 1,
    "(": 0,
    ")": 0,
}

NUMBERS = "0123456789"


def calculate(operator, operand1, operand2):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    operations = {
        "*": multiply,
        "/": divide,
        "+": add,
        "-": subtract,
    }

    return operations[operator](float(operand2), float(operand1))


def eval_infix(expression):
    operators = Stack()
    operators.push("(")
    operands = Stack()

    for token in expression.split(" "):
        if re.match(r"^\d$", token):
            operands.push(token)
        else:
            operate(token, operators, operands)
    operate(")", operators, operands)
    return operands.pop()


def operate(token, operators, operands):
    if token == "(":
        operators.push(token)
        return
    while PRECEDENCE[token] <= PRECEDENCE[operators.top()]:
        top_op = operators.pop()
        if top_op in "+-*/":
            operands.push(calculate(top_op, operands.pop(), operands.pop()))
        elif top_op == "(":
            if token == ")":
                return
            else:
                raise ValueError("Expected right parenthesis")
    operators.push(token)
    return


if __name__ == "__main__":
    print(eval_infix("( 6 + 5 ) * 4 - ( 9 + 1 )"))
