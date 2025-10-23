def suma_natural(n):
    if n == 1:
        return 1
    else:
        return n + suma_natural(n-1)

print(suma_natural(5))  # 15

