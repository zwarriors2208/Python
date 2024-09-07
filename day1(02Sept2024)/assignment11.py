# assignment 11
a = float(input("monthly income: "))
b = float(input("monthly expenses: "))

s = a - b
# expending percentage
ep = b/a * 100
# savings percentage w.r.t total income
sp = s/a * 100

print(f"total saving: {s: .2f}. \npercentage of income saved : {sp: .2f}%  \npercentage of income spent {ep: .2f}p%" )
