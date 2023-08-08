class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_green(text):
    print(f'{bcolors.OKGREEN}{text}{bcolors.ENDC}')

def print_red(text):
    print(f'{bcolors.FAIL}{text}{bcolors.ENDC}')

def print_title(text):
    print(f'{bcolors.BOLD}{bcolors.WARNING}--{text}{bcolors.ENDC}')

def print_bold(text):
    print(f'{bcolors.BOLD}|   {text}   |{bcolors.ENDC}')
    