def palindrome(number):
    original=str(number)
    reversed=original[::-1]

    if original==reversed:
        return True
    else:
        return False
num=121
if palindrome(num):
    print(f"This is a Palindrome Number {num}")
else:
    print(f"This is not a palindrome Number {num}")    

