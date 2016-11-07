from __future__ import print_function
import tempfile


tmpFile = tempfile.mktemp()
print(tmpFile)
with open(tmpFile, 'w') as f:
    print('test', file=f)
