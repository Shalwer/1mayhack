import math

all_math_func = ('acos', 'asin', 'atan', 'atan2', 'cos', 'sin', 'tan', 'ctg', )


def math_func(func, num):
    if 'pi' in num:
        pass
    else:
        num = float(num)*math.pi/180
    if func == 'acos':
        answer = math.acos(num)
        return answer
    elif func == 'asin':
        answer = math.asin(num)
        return answer
    elif func == 'atan':
        answer = math.atan(num)
        return answer
    elif func == 'cos':
        answer = math.cos(num)
        return answer
    elif func == 'sin':
        answer = math.sin(num)
        return answer
    elif func == 'ctg':
        answer = 1/(math.tan(num))
        return answer
    elif func == 'tan':
        answer = math.tan(num)
        return answer
