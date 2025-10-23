def multiplicar(a, b):
    if b == 0:
        return 0
    else:
        return a + multiplicar(a, b-1)

print(multiplicar(3, 4))  # 12

