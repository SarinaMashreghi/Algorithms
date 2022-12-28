def binary_number(s):
    n = 0
    for i in range(len(s)):
        n += int(s[len(s) - i - 1]) * 2 ** i
    return (n)


def number_binary(n):
    s = ''
    while (n > 0):
        r = n % 2
        n = n // 2
        s = str(r) + s
    return (s)


def crc(input_string, polynomial):
    polynomial_number = binary_number(polynomial)
    initial_len = len(input_string)
    length = len(polynomial)
    for i in range(len(polynomial) - 1):
        input_string += '0'
    for i in range(initial_len):
        if (input_string[i] == '1'):
            output = polynomial_number ^ binary_number(input_string[i:i + length])
            output_binary = number_binary(output)
            while (len(output_binary) < length):
                output_binary = '0' + output_binary
            input_string = input_string[:i] + output_binary + input_string[i + length:]
    return (input_string[initial_len:])


def CRC(poly, n, index):
    check[index] = int(poly[j % length]) ^ n


check = []
p = input("polynomial: ")
l = int(input("length: "))
length = len(p)
for i in range(length - 1):
    check.append(0)
j = 0
while (1 in check[:-1 * (length - 1)]) or (j < l) or (j % length != 0):
    if (j < l):
        check.insert(j, int(input()))
    if (j % length == 0):
        ind = check.index(1)
        CRC(p, check[ind], ind)
    else:
        CRC(p, check[ind], ind)
    j += 1
    ind += 1

print(check[l:])
