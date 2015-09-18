def countDown(num=0):
    print('start iteration')
    while num > 0:
        print(num)
        yield num
        num -= 1
    print('finish iteration')

count = countDown(2)
count.next()
count.next()
count.next()

