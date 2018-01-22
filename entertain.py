"""
    entertain.py-----1.Creating instances of Movies Class
                     2.Combining all movies into a list
                     3.Passing movies list as a argument to open_movies_page
                       in fresh_tomatoes.py file

     Author: Praneeth Kumar Mudumby
     Written:19-01-2018
"""
# Importing media.py ad fresh_tomatoes.py as we need to pass information

import media
import fresh_tomatoes


# Creating instances of Movie class present in media.py file
bahubali = media.Movie(
    "Bahubali 2",
    "https://vignette.wikia.nocookie.net/baahubali2662/images/7/71/Bahubali-2-Posters.jpg/revision/latest?cb=20170529020217",  # NOQA
    "https://www.youtube.com/watch?v=G62HrubdD6o")

avengers = media.Movie(
    "Avengers",
    "https://i.annihil.us/u/prod/marvel/i/mg/9/b0/55e0964dd4e2e/portrait_incredible.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

newton = media.Movie(
    "Newton",
    "https://upload.wikimedia.org/wikipedia/en/6/68/Newton_%28film%29.png",
    "https://www.youtube.com/watch?v=yU6zMPFd4UU")

alpha = media.Movie(
    "Alpha",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3MTA1MjAyNV5BMl5BanBnXkFtZTgwNzAxMzQ5MjI@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=uIxnTi4GmCo")

horror = media.Movie(
    "1921",
    "https://www.comingtrailer.com/images/poster/1921.jpg",
    "https://www.youtube.com/watch?v=kXKw2skbLdk")

dangal = media.Movie(
    "Dangal",
    "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
    "https://www.youtube.com/watch?v=x_7YlGv9u1g")

# Creating a movies list
movies = [bahubali, avengers, newton, alpha, horror, dangal]

# Calling open_movies_page by passing movies list in fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
