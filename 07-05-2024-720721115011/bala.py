def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    reversed_num = 0
    original_num = x
    while x!= 0:
        remainder = x % 10
        reversed_num = reversed_num * 10 + remainder
        x = x // 10
    return original_num == reversed_num
print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))