## Functions


# The below block of code does not take any parameters
##global variable
discount = 10


def calculate_price():
    price = 100
    tax = price * 0.1
    final_price = price + tax - discount
    print(f"Total: {final_price}")


calculate_price()


# function with arguments:
def calculate_price_arg(price, discount):
    tax = price * 0.1
    final_price = price + tax - discount
    print(f"Total: {final_price}")


calculate_price_arg(price=200, discount=10)


# with print values
def add_print(a, b):
    print(a + b)


add_print(a=10, b=20)


# with return
def add_return(a, b):
    return a + b


add_return(a=10, b=20)


# another return scenario
def simple_func():
    list_1 = [1, 2, 3, 4, 5, 6]
    return list_1[0], list_1[-3]


r1, r2 = simple_func()

print(r1, " ", r2)


# return multiple variables
def simple_func2():
    list_1 = [1, 2, 3, 4, 5, 6]
    first_num = list_1[0]
    last_num = list_1[-1]
    return first_num, last_num


first_num, last_num = simple_func2()
print(f"first_num: {first_num}; last_num: {last_num}")
