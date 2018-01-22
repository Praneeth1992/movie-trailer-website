""" media.py-----1.Creating Movie Class
                 2.Creating a function init inside Movie Class
Author: Praneeth Kumar Mudumby
Written:19-01-2018
                     """
import webbrowser
# We are creating class name Movie


class Movie():
    """
    We are creating a function init which acts like a constructor
    and taking arguments like story line,poster,trailer
    """
    def __init__(self, movie_title, movie_poster, movie_trailer):
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
