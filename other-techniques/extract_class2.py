movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]

# def send_hiring_email(email):
#     print("email sent to: ", email)
    
# for i, value in enumerate(emails):
#     if birth_year[i] > 1985:
#         print(first_names[i], last_names[i])
#         print('Movies Played: ', end='')
#         for m in movies[i]:
#             print(m, end=', ')
#         print()
#         send_hiring_email(value)

class Person:
    def __init__(self, first_name, last_name, birth_year, email, movies):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.email = email
        self.movies = movies
        
    def send_hiring_email(self, email):
        print("email sent to ", self.email)
    
    def check_movies(self):
        if self.birth_year > 1985:
            print(self.first_name, self.last_name)
            print('Movies Played: ', end='')
            for m in self.movies:
                print(m, end=', ')
            print()
            self.send_hiring_email(self.email)

Alex = Person("Alex", "Gray", 1999, "example@gmail.com", movies)

Alex.check_movies()

