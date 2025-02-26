#Class Movie is defined
import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #Instance Variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        #Plays the Movie trailer in default Web Browser
        webbrowser.open(self.trailer_youtube_url)
