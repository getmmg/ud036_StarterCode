#!python2
import json
import fresh_tomatoes
import media


'''
This creates the list of favourite movies.
'''


def fetch_from_api():
    '''
    This reads the json data from file to simulate api call.
    It should be replace with your own backend api
    '''
    movies = []
    try:
        # Open File to read the movies json
        fileHandle = open('movies.json', "r")
        data = fileHandle.read()
        # Parse the file data into Json Array
        jsonData = json.loads(data)
        for movie_data in jsonData["movies"]:
            # Create Movie class instance for all movies in json arraya
            movie = media.Movie(
                movie_data["title"],
                movie_data["poster_image_url"],
                movie_data["trailer_youtube_url"]
            )
            movies.append(movie)
    except IOError, (errno, strerror):
        print "I/O error(%s): %s" % (errno, strerror)

    finally:
        return movies


def show_movies_site():
    '''
    This fetches the list of favourite movies from api and renders the page
    '''
    movies_list = fetch_from_api()
    if movies_list:
        fresh_tomatoes.open_movies_page(movies_list)
    else:
        print "ERROR : Movies Api did not return any data"


# Calling the functon to show our website
show_movies_site()
