
tmp = 16
for i in range(1, 100):
    tmp *= 4 ** 6
    tmp %= 19
    print(f"k = {i}, remainder = {tmp}")