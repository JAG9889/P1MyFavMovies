import webbrowser

#This is the class movie which had had a few new added attributes.
class Movie () : 
    def __init__(self, movie_title, movie_synopsis, movie_genre, movie_length, poster_image_url, trailer_youtube_url) : 
                 self.title = movie_title
                 self.synopsis = movie_synopsis
                 self.genre = movie_genre
                 self.length = movie_length
                 self.poster_image_url = poster_image_url
                 self.trailer_youtube_url = trailer_youtube_url

#this function is used to open and display the movie trailer window. 
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
