valid_hex = '0123456789ABCDEF'.__contains__

def cleanhex(data):

    return ''.join(filter(valid_hex, data.upper()))

def fore_fromhex(text, hexcode):

    hex_int = int(cleanhex(hexcode), 16)
    print('\x1B[38;2;{};{};{}m{}\x1B[0m'.format(hex_int>>16, hex_int>>8&0xFF, hex_int&0xFF, text))

def back_fromhex(text, hexcode):

    hex_int = int(cleanhex(hexcode), 16)
    print('\033[48;2;{};{};{}m{}\033[0m'.format(hex_int>>16, hex_int>>8&0xFF, hex_int&0xFF, text))