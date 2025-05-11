def calculate(expression: str) -> str:
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"
