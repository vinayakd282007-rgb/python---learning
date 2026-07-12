number_of_movies = int(input("Enter number of movies: "))
movie_names = input("Enter movie names: ").split()

ratings = []
highest_rating = 0
lowest_rating = 10
excellent_movies = 0

for i in range(number_of_movies):
    rating = int(input(f"Enter rating for {movie_names[i]}: "))
    ratings.append(rating)

    if rating > highest_rating:
        highest_rating = rating

    if rating < lowest_rating:
        lowest_rating = rating

    if rating >= 8:
        excellent_movies += 1

average_rating = sum(ratings) / len(ratings)

print("\n========== Movie Rating Report ==========")
print("Movie Names:", movie_names)
print("Ratings:", ratings)
print("Highest Rating:", highest_rating)
print("Lowest Rating:", lowest_rating)
print("Average Rating:", average_rating)
print("Excellent Movies:", excellent_movies)