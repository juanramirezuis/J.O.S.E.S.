import re
from typing import Literal

class Parser:
    def __init__(self, filepath) -> None:
        try:
            with open(filepath, 'r') as f:
                self.commands = list(filter(len, [re.sub(r'//.*$', '', l).strip() for l in f]))
        except FileNotFoundError:
            print(f"Could not find {filepath}")
    
    def hasMoreCommands(self) -> bool:
        return len(self.commands) > 0

    def next(self) -> None:
        self.command = self.commands.pop(0)

    def commandType(self) -> Literal['A', 'L', 'C']:
        if self.command[0] == '@':
            return 'A_COMMAND'
        elif self.command[0] == '(' and self.command[-1] == ')':
            return 'L_COMMAND'
        return 'C_COMMAND'

    def symbol(self) -> str:
        return self.command.strip('@()')

    def dest(self) -> str:
        if '=' not in self.command:
            return ''
        return self.command.split('=')[0]

    def comp(self) -> str:
        return self.command.split('=')[-1].split(';')[0]

    def jump(self) -> str:
        if ';' not in self.command:
            return ''
        return self.command.split('=')[-1].split(';')[-1]
