import re

text = open('C:\\Users\\Julian\\Desktop\\AOC24\\03\\input.txt').read()
text_with_do = text.replace("do()", "do(1,1)").replace("don't()", "don't(1,1)")
mul_operations_with_brackets = re.findall(r"(mul|do|don't)\((\d+(?:,\d+)?)\)", text_with_do)

def calculate_mul_operations(mul):
    result_no1 = 0
    result_no2 = 0
    enable = True
    for op in mul:
        numbers = [*map(int, op[1].split(","))]
        if op[0] == "do": enable = True
        elif op[0] == "don't": enable = False
        elif op[0] == "mul" and op[1] and len(numbers) == 2:
            multiplication = numbers[0] * numbers[1]
            if enable and len(numbers) == 2:
                result_no2 += multiplication
            result_no1 += multiplication
    return result_no1, result_no2

print(calculate_mul_operations(mul_operations_with_brackets))