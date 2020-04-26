n = 13

res = 0
digit = n
aug = 0
# num = digit
# while num // 10 != 0:
#     aug += 1
#     num = num // 10

for i in range(n):
    res += digit * 10**(i + aug)
    # aug = 0
    num = digit
    while num // 10 != 0:
        aug += 1
        num = num // 10
    digit -= 1
print(res)