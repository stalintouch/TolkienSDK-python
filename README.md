
[![Python 3.7](https://www.python.org/)


# Tolkien SDK Python API

Tolkien SDK provides a simple Python-based API Lord of the Rings quotes, movies, books and all sorts of information about the Tolkien Legendarium (no Silmarilion yet though)

Note:
The book and character API are WPI at the moment but they will be available soon

## Minimum Requirements

* Python v3.7

## Compatibility
Tested compatibility for python 3.7, 3.8 and 3.9

## Quick start

### Installation of the SDK
#option 1
you can ouse the source files cloning the project
CD into the folder and run
```
python -m pip install .
```
#option 2 (Coming soon)
This SDK will be published to PIP so it can be easily installed, please stay tuned


### Instantiating and interacting with the SDK:
in order to use the API you need to provide your credentials so the SDK can interact with the LOTR API
```
Import Tolkien
client = Tolkien.Client(bearer_token=BearerToken)
```
The Client class is an objec that is used to interact with the different endpoints by resources ex: the Movie resources has an Object `MovieAPI` that is accessed through the client object. Soon to come the `BookAPI` as well as the `CharacterAPI`

BearerToken can be also set as an env variable and if you choose to do so, the bearer_token param will be ignored so you do ahve to pass it again

### Examples of using the SDK:
```
Import Tolkien
client = Tolkien.Client()

client.movieAPI.get_all_movies()
```

This will kick an API call to LOTR with the following payload:

```
{
    "docs": [
        {
            "_id": "1",
            "name": "Movie 1",
            "runtimeInMinutes": 1,
            "budgetInMillions": 1,
            "boxOfficeRevenueInMillions": 1,
            "academyAwardNominations": 1,
            "academyAwardWins": 1,
            "rottenTomatoesScore": 1
        },
    ],
    "total": 1,
    "limit": 1000,
    "offset": 0,
    "page": 1,
    "pages": 1
}
```
More examples can be found here https://the-one-api.dev/documentation


#### the MovieAPI object
Provides several methods that can be used to get information from the movies endpoint

`get_all_movies`
Gets all movies available in the movie API
Returns either a Response or API response object which will behave
very similar as far as extracting payload and error handling

`get_movie`
Gets a single movie from the movie API
Args:
    id: movie id
Returns either a Response or API response object which will behave
very similar as far as extracting payload and error handling

`get_all_movie_quotes`
Gets a all quote from an specific movie using movie id
Args:
    id: movie id
Returns either a Response or API response object which will behave
very similar as far as extracting payload and error handling

#### Working with the responses
Either if is a Response if success or custom APIResponse object if no success , they will have the same way to deal with:
`json()`
`text`
`status_code`
`ok`

so you can planned ahead and check for status code and take it from there


#### Logs

Each request is logged to the console for easy debugging and trackeability with the information below:

```
'method': req.method,
'path': path,
'status': resp.status_code,
'duration': duration,
'@timestamp': timestamp,
'@version': "1",
'host': req.headers.get('Host'),
```

## Tests

Integration and unit tests are provided with pytest, coverage, requests_mock, to run the test simply run
`pytest`
to run the test with coverage just run
`pytest --cov=. tests/`
