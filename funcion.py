from cProfile import label
from pathlib import Path
from tokenize import Number

current_path = Path.cwd()
r = 0
def porcentaje(monto,amount):
    if monto == 'Usd':
        file_path = current_path / 'usd.txt'
        file = open(file_path)
        content = file.read()
        file.close()
        r = int(content) * int(amount);
        return r
    elif monto == 'Cls':
        file_path = current_path / 'cls.txt'
        file = open(file_path)
        content = file.read()
        file.close()
        r = int(content) * int(amount);
        return r


