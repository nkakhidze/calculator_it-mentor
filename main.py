
def main(input_str: str):
    input_str = input_str.replace(" ", "")
    if not input_str:
        raise ValueError('Введена пустая строка, введите выражение типа "1 + 2"')

    operator = found_operators(input_str)
    a, b = input_str.split(operator)
    a, b = check_operand(a), check_operand(b)

    return operations_dictionary[operator](a,b)


def found_operators(input_str):
    counter = 0
    operator = ''
    for i in "+","-","*","/":
        for j in input_str:
            if j == i:
                counter += 1
                operator = j
    if counter == 0:
        raise ValueError("throws Exception //т.к. строка не является математической операцией")
    elif counter > 1:
        raise ValueError("throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")
    else:
        return operator


def check_operand(operand):
    try:
        operand = int(operand)
    except ValueError:
        raise ValueError("Калькулятор умеет работать только с целыми арабскими числами")
    if not (1 <= operand <= 10):
        raise ValueError("Калькулятор должен принимать на вход числа от 1 до 10 включительно")
    return operand


def check_only_one(input_str):
    pass


def summ(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a // b

operations_dictionary = {
    "+": summ,
    "-": sub,
    "*":mul,
    "/":div
}

print(main(input()))