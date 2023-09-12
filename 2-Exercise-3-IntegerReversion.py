def reverse_integer(n):
    reversed_integer = 0
    remainder = 0
    while n > 0:
        remainder = n % 10
        n = n // 10
        reversed_integer = (reversed_integer * 10) + remainder
    return reversed_integer


if __name__ == '__main__':
    print(reverse_integer(1234))

