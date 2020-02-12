def shex(n):
    s = bin(n)[2:]
    s = '0' * ((6 - len(s) % 6) % 6) + s
    return ''.join(chr(int(s[i: i + 6], 2) + 32) for i in range(0, len(s), 6))


def xehs(s):
    from functools import reduce
    return reduce(lambda x, y: (x << 6) + (ord(y) - 32), s, 0)


def encode(txt):
    n_repeat = [(txt.count(c), c) for c in set(txt)]
    n_repeat = sorted(n_repeat, reverse=True)  # кортежи сравниваются лексикографически

    code_characters = ''.join(c for _, c in n_repeat)
    code_book = {c: '1' * i + '0' for i, c in enumerate(code_characters)}

    code_num = ''.join(code_book[c] for c in txt)
    code_num += '0' * ((6 - len(code_num) % 6) % 6)
    code_num = shex(int(code_num, 2))

    return (len(txt), code_characters, code_num)


def decode(length, chars, code):
    code_num = bin(xehs(code))[2:]
    code_num = '0' * ((6 - len(code_num) % 6) % 6) + code_num
    decode_word = ''.join(chars[len(c)] for c in code_num.split('0'))
    return decode_word[:length]
