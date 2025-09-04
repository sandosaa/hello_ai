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
    'Sinners':[8,4,3,2,6,3]
}
while True:
    print("Available movies:")
    for movie in movies.keys():
        print("-", movie)

    user_movie = input("\nChoose a movie from the list: ".strip()).title()

    if user_movie not in movies:
        print('Movie not found')

    else:
        similarities = {}
        for movie, ratings in movies.items():
            if movie != user_movie:
                similarities[movie] = cosine_similarity(movies[user_movie], ratings)

        recommended = max(similarities, key=similarities.get)
        print(f"\nRecommended movie: {recommended}")
        print(f"Cosine similarity: {similarities[recommended]:.4f}")
        break
