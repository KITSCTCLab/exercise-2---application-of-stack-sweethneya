class Evaluate:
  def __init__(self, size):
    self.top = -1
    self.size_of_stack = size
    self.stack = []

  def isEmpty(self):  
    if len(self.stack) == 0:
        return True
    else:
        return False

  def pop(self):
    if len(self.stack) > 0:
        x = self.stack.pop()
        return x


  def push(self, operand):
    self.stack.append(operand)


  def validate_postfix_expression(self, expression):
    value = True
    valid = ['+','-','*','/']
    for char in expression:
        if char.isdigit or char in valid:
            continue
        else:
            value = False
    return value


  def evaluate_postfix_expression(self, expression):
    for char in expression:
        if char.isdigit():
            self.push(char)
        else:
            b = int(self.pop())
            a = int(self.pop())
            
            if char == "+":
                result = a + b
            elif char == "-":
                result = a - b
            elif char == '*':
                result = a * b
            elif char == '/':
                result = a / b
            self.push(result)
    return int(self.stack[0])

postfix_expression = input() # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
