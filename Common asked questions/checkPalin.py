string = input()

rev = string[::-1]

if rev == string:
    print("palindrome")
else:
    print("not palindrome")