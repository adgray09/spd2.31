# by Kami Bigdely
# Split temporary variable

patty = 70 # [gr]
pickle = 20 # [gr]
tomatoes = 25 # [gr]
lettuce = 15 # [gr]
buns = 95 # [gr]
sandwich_weight = (2 * patty + 4 * pickle + 3 * tomatoes + 2 * lettuce + 2 * buns)
print("NY Burger Weight", sandwich_weight)

kimchi = 30 # [gr]
mayo = 5 # [gr]
golden_fried_onion = 20 # [gr]
sandwich_weight = (2 * patty + 4 * pickle + 3 * tomatoes + kimchi + mayo + golden_fried_onion + 2 * buns)
print("Seoul Kimchi Burger Weight", sandwich_weight)

options = {"patty": 70, "pickle": 20, "tomatoes": 25, "lettuce": 15, "buns": 95, "Kimchi": 30, "mayo": 5, "golden_fried_onions": 20}


def make_sandwhich(dict):
    name_of_sandwhich = input("name of your sandwhich: ")
    total_weight = 0 
    for k,v in options.items():
        num_of_that_option = int(input("how many {}: ".format(k)))
        if num_of_that_option >= 1:
            total_weight += (num_of_that_option * v)
            # print(total_weight)
        elif num_of_that_option == 0:
            continue
    
    return name_of_sandwhich, total_weight

print(make_sandwhich(options))