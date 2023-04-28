from datetime import *
from pathlib import Path

name = 'bob'
last_name = 'marley_'
today = date.today()
now = datetime.now()
line = name+last_name+str(now)
file_path = Path(f'c:/check/cheklist_{today}.txt')
f = open(file_path, 'w')
f.write(line)
