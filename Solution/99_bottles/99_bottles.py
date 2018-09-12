
def count(num):
    if num == 1:
        return str(num) + ' bottle'
    elif num == 0:
        return "Go"
    else:
        return str(num) + ' bottles'


for x in range(99, -1, -1):
    if x == 0:
        print('No more bottles of beer on the wall, No more bottles of beer.')
        print('Go to the store and buy some more, ' + count(99) + ' of beer on the wall.')
    else:
        print(count(x) + ' of beer on the wall, ' + count(x) + ' of beer.')
        print('Take one down and pass it around,' + count(x-1) + ' of beer on the wall.')
    print(' ')
