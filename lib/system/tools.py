import os
import re

def clear(): os.system('clear' if os.name == 'posix' else 'cls')

def escapeAnsi(line):
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)