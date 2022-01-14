ten = input('Nhập tên: ')
print('Vậy tên của bạn là : ', ten)
n = int(input('Hãy nhập số nguyên n = '))

# kiểm tra điều kiện đúng của n
if (n < 0):
    print('Phải nhập n > 0')
else:
# Tạo dictionary
    print('Vậy dictionary được tạo là : {',end='')
    for i in range(1,n+1):
        print(' %d:%d ' %(i,i*i), end='')
        if(i<n):
            print(',',end='')
    print('}')