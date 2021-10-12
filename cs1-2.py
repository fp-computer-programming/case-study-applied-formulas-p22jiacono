#Author: JTI 10/12/21

p = input("Enter intial depoist amount: ")
r = input("Enter annual intrest rate as a percentage: ")
t = input("Enter number of years the money has been in the account: ")

a = int(p) * (((1) + (float(r) / 12)) ** (12 * int(t)))
print(a)