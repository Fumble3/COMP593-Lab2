
def main():
    
    # Creating a complex data structure
    about_me = {
        'full_name': 'Mark Henderson',
        'student_id': 10204958,
        'pizza_toppings': [
            'PEPPERONI',
            'PINEAPPLE',
            'WHITE ONION',
        ],
        'movies': [
            {'movie1': 'Free Guy',
                'title': 'Free Guy',
                'genre': 'Comedy',
                },
                {'movie2': 'The Rundown',
                    'title': 'The Rundown',
                    'genre': 'Action Comedy',
                },           
            ]        
    }
    
    print_student_name_and_id(about_me)
    
#Step 3 - Add another movie to the list of movies using the .append method
    new_movie = {'movie3': 'The Hunger Games', 'title': 'The Hunger Games', 'genre': 'Suspenseful Thriller'}
    about_me['movies'].append(new_movie)  
    return
    
#Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    student_name = ('My name is ') + about_me['full_name'] + (' but you can call me Mr. ') + about_me['full_name'][5]
    print(student_name)
    
    student_id = (about_me['student_id'])
    print('My student ID is ', (student_id))
    return
    
    
   
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    
    
    
    return





# TODO: Step 6 - Function that prints bullet list of pizza toppings
#def print_pizza_toppings(about_me):
 #   return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
#def print_movie_genres(about_me):
 #   return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
#def print_movie_titles(movie_list):
 #   return
    
if __name__ == '__main__':
    main()
    