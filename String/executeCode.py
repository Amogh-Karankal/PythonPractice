##Execute a String of Code in Python

def execute():
    loc = """
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    return fact
print(factorial(3))
    """

    exec(loc)

execute()