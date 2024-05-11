def ariphmeticOperation(symbol: str):
    typeOperation = symbol

    def operation(a: int, b: int) -> float:
        if typeOperation == '+':
            return a + b
        elif typeOperation == '-':
            return a - b
        elif typeOperation == '*':
            return a * b
        elif typeOperation == '/':
            return a / b
        else:
            return f'operation \"{typeOperation}\" has no realisation'

    return operation

sumNumbers = ariphmeticOperation('+')
value1 = 2
value2 = 5

sumresult = sumNumbers(value1, value2)
print(sumresult)

diffNumbers = ariphmeticOperation('-')
value1 = 2
value2 = 5

diffresult = diffNumbers(value1, value2)
print(diffresult)

multNumbers = ariphmeticOperation('*')
value1 = 2
value2 = 5

multresult = multNumbers(value1, value2)
print(multresult)

fracNumbers = ariphmeticOperation('/')
value1 = 2
value2 = 5

fracresult = fracNumbers(value1, value2)
print(fracresult)

