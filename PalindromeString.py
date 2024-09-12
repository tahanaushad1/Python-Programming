def palindromeString(s):
    orginal = str(s)
    reversed=s[::-1]
    if orginal==reversed:
        return True
    else:
        return False
    
string="madam"
if palindromeString(string):
    print(f"This is Palindrome String  {string}")
else:
    print(f"This is not a palindrome String {string}")        