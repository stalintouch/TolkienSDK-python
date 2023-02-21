

class MovieEndpoint():
    movies = '/movie'
    movie = '/movie/{id}'
    movie_quotes = '/movie/{id}/quote'


class APIErrorMessage:
    movies_not_returned = 'no movies returned from API'
    movie_not_found = 'no movie found with the id of {id}'
    movie_not_quotes_found = 'no movie quotes found for the movie id {id}'
    unauthorized = 'The server returned a 401 unauthorized please check the Bearer token is correct and is valid'
