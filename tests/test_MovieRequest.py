from Tolkien.strings import MovieEndpoint


BASE_URL = 'https://the-one-api.dev/v2'


def test_get_all_movies(mock_movie_req, mock_all_movies_payload, requests_mock):
    url = BASE_URL + MovieEndpoint.movies

    requests_mock.get(url, status_code=200, json=mock_all_movies_payload)
    resp = mock_movie_req.get_all_movies()
    movies = resp.json().get('docs')

    assert resp.ok
    assert resp.json().get('total') == 8
    assert len(movies) == 8
    assert movies[0].get('_id') == str(1)
    assert movies[0].get('name') == 'Movie 1'


def test_get_all_movies_unauthorized(mock_movie_req, requests_mock):
    url = BASE_URL + MovieEndpoint.movies
    message = {"ok": False, "text": "Unauthorized.", "status_code": 401}
    requests_mock.get(url, status_code=401, json=message)

    resp = mock_movie_req.get_all_movies()

    assert resp.ok is False
    assert resp.json().get('text') == 'no movies returned from API'
    assert resp.json().get('status_code') == 401


def test_get_movie(mock_movie_req, requests_mock, mock_single_movie_payload):
    url = BASE_URL + MovieEndpoint.movie.format(id=1)
    requests_mock.get(url, status_code=200, json=mock_single_movie_payload)

    resp = mock_movie_req.get_movie(id=1)
    movie = resp.json().get('docs')

    assert resp.ok
    assert resp.json().get('total') == 1
    assert len(movie) == 1
    assert movie[0].get('_id') == str(1)
    assert movie[0].get('name') == 'Movie 1'


def test_get_single_movie_unauthorized(mock_movie_req, requests_mock):
    url = BASE_URL + MovieEndpoint.movie.format(id=1)
    message = {"ok": False, "text": "Unauthorized.", "status_code": 401}
    requests_mock.get(url, status_code=401, json=message)

    resp = mock_movie_req.get_movie(id=1)

    assert resp.ok is False
    assert resp.json().get('text') == 'no movie found with the id of 1'
    assert resp.json().get('status_code') == 401


def test_get_all_movie_quotes(mock_movie_req, mock_all_movies_payload, requests_mock, mock_all_quotes):
    url = BASE_URL + MovieEndpoint.movie_quotes.format(id=1)

    requests_mock.get(url, status_code=200, json=mock_all_quotes)
    resp = mock_movie_req.get_all_movie_quotes(1)
    movies = resp.json().get('docs')

    assert resp.ok
    assert resp.json().get('total') == 382
    assert len(movies) == 382
    assert movies[0].get('_id') == str(1)
    assert movies[0].get('dialog') == 'I will break him.'


def test_get_all_movie_quotes_unauthorized(mock_movie_req, requests_mock):
    url = BASE_URL + MovieEndpoint.movie_quotes.format(id=1)
    message = {"ok": False, "text": "Unauthorized.", "status_code": 401}
    requests_mock.get(url, status_code=401, json=message)

    resp = mock_movie_req.get_all_movie_quotes(1)

    assert resp.ok is False
    assert resp.json().get('text') == 'no movie quotes found for the movie id 1'
    assert resp.json().get('status_code') == 401
