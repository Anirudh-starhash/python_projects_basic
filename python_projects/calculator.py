import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {'+': add, '-': sub, '*': mul, '/': div}


def calculator():
    while should_continue:
        num2 = int(input('enter the second number:'))
        for x in operations:
            print(x)
        op = input('enter the operation you want to practice')
        function = operations[op]
        ans = function(num1, num2)
        print(
            f"enter the first number is {num1} and the second number is {num2} and the answer for the function {function} is {ans}"
        )
        

num1 = int(input('enter the first number:'))
should_continue=True
calculator()
