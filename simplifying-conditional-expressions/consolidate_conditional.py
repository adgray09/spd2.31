# by Kami Bigdely
# Consolidate conditional expressions
def dice(ingredients):
    print("diced all ingredients.")
def mix_all(diced_ingredients):
    print("mixed all.")
def add_salt():
    print('added salt.')
def pour(liquid):
    print('poured', liquid + '.',)
    
    
def lacks_ingredients(ingredients):
    
    necessary_ingredients = {
        'cucumber': False,
        'tomato': False,
        'onion': False,
        'lemon juice': False
    }
    
    for ingredient in ingredients:
        necessary_ingredients[ingredient] = True
    for _, value in necessary_ingredients.items():
        if not value:
            return True
    return False

def make_shirazi_salad(ingredients):
    if lacks_ingredients(ingredients):
        print('lacks ingredients')
        return
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')

if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
