from requests import Response
from typing import Union

from Tolkien.requests.SDKRequest import SDKRequest
from Tolkien.models.APIResponse import APIResponse
from Tolkien.strings import APIErrorMessage, MovieEndpoint


class MovieRequest():
    '''
        Object use to interact with the movie resources
    '''
    def __init__(self) -> None:
        self.request = SDKRequest()

    def get_all_movies(self) -> Union[Response, APIResponse]:
        '''
            Gets all movies available in the movie API

            Returns either a Response or API response object which will behave
            very similar as far as extracting payload and error handling
        '''
        resp = self.request.make_request('GET', MovieEndpoint.movies)

        if not resp.ok:
            return APIResponse(resp.status_code, False, APIErrorMessage.movies_not_returned)

        return resp

    def get_movie(self, id) -> Union[Response, APIResponse]:
        '''
            Gets a single movie from the movie API

            Args:
                id: movie id

            Returns either a Response or API response object which will behave
            very similar as far as extracting payload and error handling
        '''
        url = MovieEndpoint.movie.format(id=id)
        resp = self.request.make_request('GET', url)

        if not resp.ok:
            return APIResponse(resp.status_code, False, APIErrorMessage.movie_not_found.format(id=id))

        return resp

    def get_all_movie_quotes(self, id) -> Union[Response, APIResponse]:
        '''
            Gets a all quote from an specific movie using movie id

            Args:
                id: movie id

            Returns either a Response or API response object which will behave
            very similar as far as extracting payload and error handling
        '''
        url = MovieEndpoint.movie_quotes.format(id=id)
        resp = self.request.make_request('GET', url)

        if not resp.ok:
            return APIResponse(resp.status_code, False, APIErrorMessage.movie_not_quotes_found.format(id=id))

        return resp

    # Other methods to expose to the API later
    # def get_quotes_sorted(self, params, **kwards)
    # def get_filtered_movie(self, params, **kwards) 
    # def get_movie_sorted(self, params, **kwards)