def inverse(s):
    return s[::-1]

def main():
    s = "ABCDEFGH"
    reversed_s = inverse(s)
    for i in range(1, len(reversed_s), 2):
        print(reversed_s[i], end='')

main()