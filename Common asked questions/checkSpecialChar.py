import re

str = input()

regex = re.compile('[$&+,:;=?@#|<>^*()%!-]')

if(regex.search(str)):
    print("contains special characters")

else:
    print("doesn't contain special characters")
