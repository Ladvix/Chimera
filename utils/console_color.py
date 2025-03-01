valid_hex = '0123456789ABCDEF'.__contains__

# ANSI escape codes for text styling
COLORS = {
    'BLACK': '\033[30m',
    'RED': '\033[31m',
    'GREEN': '\033[32m',
    'YELLOW': '\033[33m',
    'BLUE': '\033[34m',
    'MAGENTA': '\033[35m',
    'CYAN': '\033[36m',
    'WHITE': '\033[37m',
    'RESET': '\033[0m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
    'REVERSE': '\033[7m'
}

def cleanhex(data):
    return ''.join(filter(valid_hex, data.upper()))

def fore_fromhex(text, hexcode):
    hex_int = int(cleanhex(hexcode), 16)
    print('\x1B[38;2;{};{};{}m{}\x1B[0m'.format(hex_int>>16, hex_int>>8&0xFF, hex_int&0xFF, text))

def back_fromhex(text, hexcode):
    hex_int = int(cleanhex(hexcode), 16)
    print('\033[48;2;{};{};{}m{}\033[0m'.format(hex_int>>16, hex_int>>8&0xFF, hex_int&0xFF, text))

def print_styled(text, style=None, hex_color=None):
    """Print text with predefined style or hex color"""
    if hex_color:
        fore_fromhex(text, hex_color)
    elif style and style.upper() in COLORS:
        print(f"{COLORS[style.upper()]}{text}{COLORS['RESET']}")
    else:
        print(text)

def print_header(text, hex_color='#FF4C2D'):
    """Print a styled header with optional color"""
    print()
    fore_fromhex(f"{COLORS['BOLD']}{text}{COLORS['RESET']}", hex_color)
    print()

def print_success(text):
    """Print a success message"""
    print_styled(f"{text}", 'GREEN')

def print_error(text):
    """Print an error message"""
    print_styled(f"{text}", 'RED')

def print_info(text):
    """Print an info message"""
    print_styled(f"ℹ {text}", 'CYAN')

def print_warning(text):
    """Print a warning message"""
    print_styled(f"⚠ {text}", 'YELLOW')

def print_step(step_number, text):
    """Print a step in a process"""
    print_styled(f"[{step_number}] {text}", 'BLUE')

def print_input_prompt(prompt_text):
    """Print an input prompt with styling"""
    return input(f"{COLORS['BOLD']}{COLORS['CYAN']}{prompt_text}{COLORS['RESET']} ")