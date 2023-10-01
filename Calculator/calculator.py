# Author Name - Raghav Singh
# Date - 05/12/2023
# file - calculator.py
# description -calculator that will caculate the expression based on the operators and operands.

from stack import Stack
from tree import ExpTree
def infix_to_postfix(infix):
    postfix_stack = Stack()
    operator_stack = Stack()
    precedence = {'^':3,'*':2,'/':2,'+':1,'-':1}
    prev = False
    for i in infix:
        if i.isdigit() or i == '.':
                if postfix_stack.isEmpty():
                    postfix_stack.push(i)
                elif i == '.':
                    postfix_stack.push(postfix_stack.pop()+i)
                
                elif prev:
                    postfix_stack.push(postfix_stack.pop()+i)
                else:
                    postfix_stack.push(i)
        elif i in precedence:
            while (not operator_stack.isEmpty() and
                   operator_stack.peek() != '(' and
                   precedence[operator_stack.peek()] >= precedence[i]):
                postfix_stack.push(operator_stack.pop())
            operator_stack.push(i)
        elif i == '(':
            operator_stack.push(i)
        elif i == ')':
            while operator_stack.peek() != '(':
                postfix_stack.push(operator_stack.pop())
            operator_stack.pop()
        prev = i.isdigit() or i == '.'
    while not operator_stack.isEmpty():
        postfix_stack.push(operator_stack.pop())
    ans=""
    while not postfix_stack.isEmpty():
        ans=postfix_stack.pop()+ ' ' + ans
    return ans[:-1]


def calculate(infix):
        postfix = infix_to_postfix(infix).split()
        expression_tree = ExpTree.make_tree(postfix)
        result = ExpTree.evaluate(expression_tree)
        return result
# a driver to test calculate module




if __name__ == '__main__':
    print("Welcome to Calculator Program!")
    while True:
        lalla = input("Please enter your expression here. To quit enter 'quit' or 'q': ")
        print("\n")
        if lalla.lower() == "quit" or lalla.lower() == "q":
            print("Goodbye!")
            break
        else:
            result = calculate(lalla)
            print(f"{result}")
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'
    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
