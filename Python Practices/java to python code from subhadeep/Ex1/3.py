sales = int(input())
if sales>=0 and sales<20000:
    print(f"3% commission rate and Rs {sales*0.03} commission ammount")
elif sales>=20000 and sales<50000:
    print(f"12% commission rate and Rs {sales*0.12} commission ammount")
else:
    print(f"31% commission rate and Rs {sales * 0.12} commission ammount")