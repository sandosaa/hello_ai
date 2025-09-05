def x_dot_y(X, Y):
    return sum(i * j for i, j in zip(X, Y))

def norm(vec):
    return sum(v**2 for v in vec) ** 0.5

def cosine_similarity(X, Y):
    return x_dot_y(X, Y) / (norm(X) * norm(Y))


movies = {
    'The Shawshank Redemption':[9.2,6.5,5,6.8,6.2,6],
    'The Godfather':[9.7,7.2,4.5,6.5,7.5,7],
    'The Dark Knight':[8.8,9.3,7,6.8,7.8,7.2],
    '12 Angry Men':[9.6,2.5,3,5.5,5.8,3.5],
    'Inception':[8.5,9,9.4,6,6.8,7.5],
    'The Matrix':[8,9.5,9.6,6,6.5,7.2],
    'It\'s A Wonderful Life':[9.2,4.5,6.5,7.8,4,8.5],
    'Captain America: Brave New World':[5,7,6,5,2,3],
    'Heads Of State':[4,8,1,7,1,2],
    'Sikandar':[4,6,1,2,1,3],
    'Get Out':[8,5,2,6,9,3],
    'Titanic':[9,5,1,2,2,10],
    'Infinity War':[6,9,9,3,2,3],
    'Avatar':[7,9,10,3,2,4],
    'The Babadook':[9,3,1,2,9,2],
    'The Shape Of Water':[8,4,7,3,2,8],
    'Everything Everywhere All At Once':[8,7,7,7,3,6],
    'Bird Box':[6,5,3,1,7,2],
    'Parasite':[9,3,2,6,5,4],
    'Moonlight':[9,1,1,2,1,6],
    'Sinners':[8,4,3,2,6,3],
    'No Time to Die':[8,9,6,5,4,7],
    'Dune':[8,6,10,2,3,4],
    'Old':[7,4,7,3,6,2],
    'Hocus Pocus':[5,3,2,7,4,3],
    'Cruella':[6.5,7,1,7,2,3],
    'Promising Young Woman':[9,3,1,7,5,4],
    'Knives Out':[7,3,1,8,2,2],
    'Forrest Gump':[9,2,1,7,1,6],
    '3 Idiots':[8,2,1,9,1,4],
    'Black Bag':[7,8,2,2,1,3],
    'Pulpa Fiction':[8,8,0,6,3,2],
    'The Batman':[8,9,2,2,3,3],
    'A Quiet Place':[7,6,7,1,9,3],
    'hereditary':[8,2,0,1,10,1],
    'The Northman':[8,9,0,2,3,3],
    'The Menu':[7,3,0,7,8,2],
    'Don\'t Look Up':[6,3,8,8,2,2],
    'The Whale':[10,1,0,2,1,4],
    'The Lighthouse':[8,2,0,2,9,1],
    'Arrival':[9,5,10,2,3,4]
}

while True:
    similarities = {}
    print("\nAvailable movies:\n")
    for movie in movies.keys():
        print("-", movie)
    while True:

        choice=input('If you want add your own rate enter "1" and if you want choose the movie enter "2": ')

        if choice == '2':
    
            user_movie = input("\nChoose a movie from the list: ".strip()).title()

            if user_movie not in movies:
                print('\nMovie not found, Try again!')

            else:
                
                for movie, ratings in movies.items():
                    if movie != user_movie:
                        similarities[movie] = cosine_similarity(movies[user_movie], ratings)
                recommended = max(similarities, key=similarities.get)
                print(f"\nRecommended movie: {recommended}")
                print(f"With Similarity: {similarities[recommended]*100:.2f}%\n")
                top_3 = []
                for i in range(3):
                    best_movie = max(similarities, key=similarities.get)
                    print(i+1,"-",best_movie)
                    top_3.append((best_movie, similarities[best_movie]))
                    del similarities[best_movie]
                break
        

        if choice =='1':
            usr_rate=[]
            types_movie=['Drama','Action','Sci-fi','Comedy','Scary','Romantic']
            print('Enter your rate from 1 to 10 for each type.')
            for i in range(6):
                #Drama,Action,Sci-fi,Comedy,Scary,Romantic
                try:
                    usr_input = float(input(f'{types_movie[i]}: '))
                except ValueError: 
                    print('Please enter a valid input!')
                    break  
                if usr_input>10 or usr_input<0:
                    print('You cant enter a number more than 10 or less than 0.')
                    usr_input = float(input(types_movie[i],': '))
                usr_rate.append(usr_input)
            if norm(usr_rate)==0:
                print('You can not enter all rates = 0 !')
                break
            else:

                for movie, ratings in movies.items():
                    similarities[movie] = cosine_similarity(usr_rate, ratings)

                recommended = max(similarities, key=similarities.get)
                print(f"\nRecommended movie: {recommended}")
                print(f"With Similarity: {similarities[recommended]*100:.2f}%\n")
                break
            
        else:
            print('You entered invaild input!')        
            choice=input('If you want add your own rate enter "1" and if you want choose the movie enter "2": ')

    usr = input('Do you want to continue? (y/n): ').strip().lower()
    if usr =='y':
        pass 
    elif usr == 'n':
        print('Byeeeeeeeee<3')
        break
    else:
        print('You entered invalid input,but Goodbye!')
    



                





            



        
