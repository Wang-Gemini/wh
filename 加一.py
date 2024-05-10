def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            break
    else:
        return [1] + digits
    return digits

print(plusOne([1, 2, 3]))
