# By Kami Bigdely
# Split temp variable

def save_into_db():
    user_input = input('Please enter your username: ')
    age = 2020 - user_input
    print("saved into database")
    print("You are",age, "years old.")
    return age,user_input


save_into_db()

