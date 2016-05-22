with open('/etc/passwd') as f:
    for line in iter(f.read, ''):
        print(line)
