hoten = input('Nhập đầy đủ họ và tên : ')
print('Họ và tên của bạn là : ', hoten)
n = int(input('Nhập số nguyên dương n = '))
m = n
dao = 0
while (m > 0):
    dao = dao * 10 + m % 10
    m = m // 10
if (dao == n):
    print('Vậy %d là số thuận nghịch' %n)
else:
    print('Vậy %d không phải số thuận nghịch' %n)