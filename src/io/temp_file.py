from tempfile import NamedTemporaryFile
from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    f.write('test')
    f.seek(0)
    print(f.read())


with NamedTemporaryFile('w+t', delete=True) as f:
    print(f.name)
