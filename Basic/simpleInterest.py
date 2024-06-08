def simple_interest(p, r, t):
    answer = (p * r * t)/100
    return answer

p = float(input("Enter principle amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

print("The simple interest is: ", simple_interest(p,r,t))