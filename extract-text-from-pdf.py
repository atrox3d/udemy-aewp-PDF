from pathlib import Path
import fitz

file_path = list(Path('files/').glob('*.pdf'))[0]
file_path = 'students.pdf'


with fitz.open(file_path) as pdf:
    for page in pdf:
        print('-' * 20)
        print(page.get_text())
