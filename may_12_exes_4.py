def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count

def is_composite(n):
    return n > 1 and not is_prime(n)

def main():
    l = int(input("Введите начало интервала (l): "))
    r = int(input("Введите конец интервала (r): "))

    count = 0
    for num in range(l, r + 1):
        if is_composite(num):
            num_divisors = count_divisors(num)
            if is_prime(num_divisors):
                count += 1

    print("Количество составных чисел с простым числом делителей:", count)

if __name__ == "__main__":
    main()
