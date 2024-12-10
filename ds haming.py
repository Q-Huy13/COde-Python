def generate_hamming_numbers(n):
    hamming = [1]  
    i2 = i3 = i5 = 0  
    mul_2,mul_3, mul_5 = 2, 3, 5
    for _ in range(1, n):
        next_hamming = min(mul_2, mul_3,mul_5)
        hamming.append(next_hamming)
        if next_hamming == mul_2:
            i2 += 1
            mul_2 = hamming[i2] * 2
        if next_hamming == mul_3:
            i3 += 1
            mul_3 = hamming[i3] * 3
        if next_hamming == mul_5:
            i5 += 1
            mul_5 = hamming[i5] * 5
    return hamming
def vi_tri(number, n=1000):
    hamming_numbers = generate_hamming_numbers(n)
    if number in hamming_numbers:
        return hamming_numbers.index(number) + 1  # Trả về vị trí (bắt đầu từ 1)
    else:
        return 'Not in sequence'
for _ in range(int(input())):
    a=int(input())
    print(vi_tri(a))

