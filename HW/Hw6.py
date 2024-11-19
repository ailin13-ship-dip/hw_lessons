def power(a, b):
    result = 1
    while b > 0:
        if b % 2 == 1:  # если степень нечётная
            result *= a
        a *= a  # возводим основание в квадрат
        b //= 2  # делим степень пополам
    return result

base = 3
exponent = 5
print(f"{base} в степени {exponent} равно {power(base, exponent)}")
