valid_hex = '0123456789ABCDEF'.__contains__

def cleanhex(data):
    return ''.join(filter(valid_hex, data.upper()))

def fore_fromhex(text, hex_color):
    """Print a styled text with fore color"""
    hex_int = int(cleanhex(hex_color), 16)
    return '\x1B[38;2;{};{};{}m{}\x1B[0m'.format(hex_int>>16, hex_int>>8&0xFF, hex_int&0xFF, text)

def back_fromhex(text, hex_color):
    """Print a styled text with back color"""
    hex_int = int(cleanhex(hex_color), 16)
    return '\033[48;2;{};{};{}m{}\033[0m'.format(hex_int>>16, hex_int>>8&0xFF, hex_int&0xFF, text)

def print_success(text):
    """Print a success message"""
    print(fore_fromhex(text, '#08FF00'))

def print_error(text):
    """Print an error message"""
    print(fore_fromhex('▶ ' + text, '#FF4C2D'))

def print_info(text):
    """Print an info message"""
    print(fore_fromhex('ⓘ ' + text, '#008BFF'))

def print_log(text):
    """Print an info message"""
    print(fore_fromhex('▶ ' + text, '#008BFF'))

def print_warning(text):
    """Print a warning message"""
    print(fore_fromhex('⚠ ' + text, '#FF4C2D'))

def print_input_prompt(prompt_text):
    """Print an input prompt with styling"""
    return input(fore_fromhex('▶ ' + prompt_text, '#008BFF'))