def simple():
    print("I am a function")
simple()

def gbp_to_usd(gbp):
    usd = gbp*1.5
    return usd

usd = gbp_to_usd(5)
print(usd)
usd = gbp_to_usd(1.2)
print(usd)
usd = gbp_to_usd(5213)
print(usd)
