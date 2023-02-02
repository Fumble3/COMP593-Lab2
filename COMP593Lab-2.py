def main():
    # Create the complex data structure
    data_table = {
        'name': 'Mark Henderson',
        'student_id': 10204958,
        'pizza_toppings': [
            'Pepperoni',
            'Pineapple',
            'Bacon',
        ],
        'movies': [
            {'title': 'Get Hard',
            'genre': 'Comedy',
            },
            {'title': 'Deadpool',
            'genre': 'Comedy',
            }
        ]
}

    sentence(data_table)
    

   
# Add one more movie to the list    
    new_movie = {'title': 'The Hunger Games', 'genre': 'Suspenseful Thriller',}
    data_table['movies'].append(new_movie)
    
#Adding toppings to the list and sorting them
def add_toppings(data_table, new_toppings):
    
    new_toppings = ('Olives', 'Chicken', 'Onion')
    data_table['pizza_toppings'].append(new_toppings)
    
    sort_toppings = sorted(data_table['pizza_toppings']())
    print(sort_toppings)

def sentence(data_table):
    
    print("My name is", data_table['name'],"but you can call me Mr.", data_table['name'][5])
    print("My student ID is", data_table['student_id'])
    print('My favourite pizza toppings are: ')
    
    for d in data_table['pizza_toppings']:
        print(d)

    print ('I like to watch', data_table['movies'],'movies.')
   
  

if __name__ == '__main__':
    main()