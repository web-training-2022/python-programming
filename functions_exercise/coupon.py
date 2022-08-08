# https://docs.python.org/3/library/operator.html
coupons = ["FIRST5", "FRIDAYSPL", "WELCOME"]

def set_coupons(**data):
    coupons_source = {}
    for key in data:
        if key in coupons:
            coupons_source.update({key: data[key]})
    print(coupons_source)
    def get_final_amount(amount, coupon=None):
        return amount - coupons_source.get(coupon, 0)
    return get_final_amount

apply_coupon = set_coupons(FIRST5=500, FRIDAYSPL=1000, WELCOME=1500)

# when we apply coupon with 50,000 we must get set discount
print("Applying FIRST5 coupon to 50,000:")
print(apply_coupon(50000, coupon="FIRST5"))
print("Applying FRIDAYSPL coupon to 50,000:")
print(apply_coupon(50000, coupon="FRIDAYSPL"))
print("Applying WELCOME coupon to 50,000:")
print(apply_coupon(50000, coupon="WELCOME"))
print("Applying INVALID coupon to 50,000:")
print(apply_coupon(50000, coupon="INVALID"))

# setting prime_user_coupons
print("")
prime_user_coupons = set_coupons(FIRST5=600, FRIDAYSPL=1100, WELCOME=1700)
print("Applying FIRST5 coupon to 50,000 for prime user:")
print(prime_user_coupons(50000, coupon="FIRST5"))
print("Applying FRIDAYSPL coupon to 50,000 for prime user:")
print(prime_user_coupons(50000, coupon="FRIDAYSPL"))
print("Applying WELCOME coupon to 50,000 for prime user:")
print(prime_user_coupons(50000, coupon="WELCOME"))
print("Applying INVALID coupon to 50,000 for prime user:")
print(prime_user_coupons(50000, coupon="INVALID"))




# returning function
def exernal_fun(*values):
    def inner_fun():
        return values[0]
    return inner_fun

this = exernal_fun(10,20,30)
# this is a function & you can call it like this:
output_value = this()


# returning function executed
def exernal_fun(*values):
    def inner_fun():
        return values[0]
    return inner_fun()

output_value = exernal_fun(10,20,30) 
# since return is function call, it gets executed and returns you final output
