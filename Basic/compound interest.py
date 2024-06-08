def ci(p, r, t):
    a = p * (pow((1 + (r/100)), t))
    ci = a - p

    return ci

p = float(input("Enter principle amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

print("The compound interest is: ", ci(p,r,t))