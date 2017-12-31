#!python2
import webbrowser


class Movie:
    '''
    This Class is the model for our movie website.
    A New instance of this would be created to for every movie
    '''
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        '''
        3 instance variables title, poster_image_url, youtube_url is required
        Make changes to this function depending on output from movies api
        '''
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
