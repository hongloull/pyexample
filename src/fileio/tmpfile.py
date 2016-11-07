from tempfile import TemporaryFile, NamedTemporaryFile

with TemporaryFile('w+') as f:
    f.write('write tempfile')
    f.seek(0)
    print(f.read())

with NamedTemporaryFile('w+', delete=False) as f:
    f.write('write tempfile')
    print(f.name)

# require Python3
# from tempfile import TemoraryDirectory
