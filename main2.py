# numbers = [1,2,3,4]
# # Cach 1
# squares_nums = []
# for i in numbers:
#     squares_nums.append(i**2)
# print(squares_nums)
# # Cach 2
# squares_nums2 = [i**2 for i in numbers]
# print(squares_nums2)
# # Cach 3
# squares_nums3 = list(map(lambda x: x**2, numbers))
# print(squares_nums3)
# Ham filter
# VD: Tao danh sach cac so nguyen to < 100000
# Dinh nghia ham kiem tra SNT
def is_prime(n):
    if n < 2 : return False
    for i in range(2, n//2+1):
        if n % i == 0: return False
    return True
n = 100000
prime_nums = list(filter(is_prime, range(2,n)))
for n in prime_nums:
    print(n, end=" ")
