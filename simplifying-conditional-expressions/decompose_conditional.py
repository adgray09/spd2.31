# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('!!!')
    print('there is a toxin in the food!')
    print('!!!')
    print('made alert sound.')
def make_accept_sound():
    print('***')
    print('Toxin Free')
    print('***')
    print('made acceptance sound')

def has_toxic_ingredients(ingredients):
    toxic_ingredients = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']
    for ingredient in ingredients:
        if ingredient in toxic_ingredients:
            return True
    return False

ingredients = ['sodium benzoate']
if has_toxic_ingredients(ingredients):
    make_alert_sound()
else:
    make_accept_sound()