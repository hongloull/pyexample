import io

f=io.StringIO()
f.write(u'qoenfnzcnbv')
for l in f:
    print(l)

from tempfile import NamedTemporaryFile

