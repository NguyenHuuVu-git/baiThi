tendem = input('Nhập tên đệm và tên vào : ')
print('Vậy tên đệm và tên bạn là : ', tendem)
n = int(input('Hãy nhập số nguyên dương n = '))

tong = 0
print('Vậy tổng các chữ số của n là : ')

while (n > 0):
    tong = tong + n % 10
    print(' %d ' % (n % 10), end='')
    if(n > 9):
        print('+', end='')
    n = n // 10

print(' = %d' %tong)
