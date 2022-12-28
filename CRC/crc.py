def binary_number(s):
    n=0
    for i in range(len(s)):
        n+=int(s[len(s)-i-1])*2**i
    return(n)

def number_binary(n):
    s=''
    while(n>0):
        r=n%2
        n=n//2
        s=str(r)+s
    return(s)

def crc(input_string,polynomial):
    polynomial_number=binary_number(polynomial)
    initial_len=len(input_string)
    length = len(polynomial)
    for i in range(len(polynomial)-1):
        input_string+='0'
    for i in range(initial_len):
        if(input_string[i]=='1'):
            output=polynomial_number^binary_number(input_string[i:i+length])
            output_binary=number_binary(output)
            while(len(output_binary)<length):
                output_binary='0'+output_binary
            input_string= input_string[:i] + output_binary + input_string[i+length:]
    return(input_string[initial_len:])

s='111111111111111110101010101010101010101010101010'
# for i in range (32):
#     s+='10'
p=input()
print(crc(s,p))
#print(s)