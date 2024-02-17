def convert_to_base(base: int, num: str):
    if not (2 <= base <= 36):
        return ("base exceeds limit")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while num > 0:
        remainder = num % base
        result = digits[remainder] + result
        num = num // base

    return result

def convert_from_base(base: int, num: str) -> int:
    if not (2 <= base <= 36):
        return "Base must be between 2 and 36"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = num.upper()
    result = 0

    for i, digit in enumerate(num):
        if digit not in digits[:base]:
            return "Invalid number for the given base"

        value = digits.index(digit)
        power = len(num) - i - 1
        result += value * (base ** power)

    return result