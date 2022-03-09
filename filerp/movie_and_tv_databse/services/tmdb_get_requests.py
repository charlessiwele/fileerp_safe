import requests
from config.Config import Config


def get_languages_url():
    return 'https://api.themoviedb.org/3/configuration/languages?api_key={}'


def get_jobs_url():
    return 'https://api.themoviedb.org/3/configuration/jobs?api_key={}'


def get_countries_url():
    return 'https://api.themoviedb.org/3/configuration/countries?api_key={}'


def get_movie_genres_url(language=None):
    if language:
        return 'https://api.themoviedb.org/3/genre/movie/list?api_key={}&language=' + language
    return 'https://api.themoviedb.org/3/genre/movie/list?api_key={}'


def get_tv_genres_url(language=None):
    if language:
        return 'https://api.themoviedb.org/3/genre/tv/list?api_key={}&language=' + language
    return 'https://api.themoviedb.org/3/genre/tv/list?api_key={}'


def get_movie_details_by_id_url(movie_id, language=None):
    if language:
        return f'https://api.themoviedb.org/3/movie/{movie_id}' + '?api_key={}&language=' + language
    return f'https://api.themoviedb.org/3/movie/{movie_id}?' + 'api_key={}'


def get_movie_credits_by_id_url(movie_id, language=None):
    if language:
        return f'https://api.themoviedb.org/3/movie/{movie_id}/credits?' + 'api_key={}&language=' + language
    return f'https://api.themoviedb.org/3/movie/{movie_id}/credits?' + 'api_key={}'


def get_movie_images_by_id_url(movie_id, language=None):
    if language:
        return f'https://api.themoviedb.org/3/movie/{movie_id}/images?' + 'api_key={}&language=' + language
    return f'https://api.themoviedb.org/3/movie/{movie_id}/images?' + 'api_key={}'


def get_movie_latest_by_id_url(language=None):
    if language:
        return f'https://api.themoviedb.org/3/movie/latest?' + 'api_key={}&language=' + language
    return f'https://api.themoviedb.org/3/movie/latest?' + 'api_key={}'


def get_movie_recommendations_by_id_url(movie_id, language=None, page=1):
    if language:
        return f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?page={page}&' + 'api_key={}&language=' + language
    return f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?page={page}&' + 'api_key={}'


def get_movie_now_playing_by_id_url(language=None, page=1):
    if language:
        return f'https://api.themoviedb.org/3/movie/now_playing?page={page}&' + 'api_key={}&language=' + language
    return f'https://api.themoviedb.org/3/movie/now_playing?page={page}&' + 'api_key={}'


def get_movie_now_playing_by_id_url(language=None, page=1):
    if language:
        return f'https://api.themoviedb.org/3/movie/top_rated?page={page}&' + 'api_key={}&language=' + language
    return f'https://api.themoviedb.org/3/movie/top_rated?page={page}&' + 'api_key={}'


def get_movie_upcoming_by_id_url(language=None, page=1):
    if language:
        return f'https://api.themoviedb.org/3/movie/upcoming?page={page}&' + 'api_key={}&language=' + language
    return f'https://api.themoviedb.org/3/movie/upcoming?page={page}&' + 'api_key={}'


def get_movie_search_by_query_url(query, language=None, page=1):
    if language:
        return f'https://api.themoviedb.org/3/search/movie?page={page}&query={query}&' + 'api_key={}&language=' + language
    return f'https://api.themoviedb.org/3/search/movie?page={page}&query={query}&' + 'api_key={}'


def get_tv_search_by_query_url(query, language=None, page=1):
    if language:
        return f'https://api.themoviedb.org/3/search/tv?page={page}&query={query}&' + 'api_key={}&language=' + language
    return f'https://api.themoviedb.org/3/search/tv?page={page}&query={query}&' + 'api_key={}'


def get_movie_popular_by_id_url(language=None, page=1):
    if language:
        return f'https://api.themoviedb.org/3/movie/popular?page={page}&' + 'api_key={}&language=' + language
    return f'https://api.themoviedb.org/3/movie/popular?page={page}&' + 'api_key={}'


def get_movie_alternative_titles_by_id_url(movie_id):
    return f'https://api.themoviedb.org/3/movie/{movie_id}/alternative_titles?' + 'api_key={}'


def get_discover_movies_url(sort_by=None, include_adult=None, include_video=None, page=None,
                            with_watch_monetization_types=None, language=None):
    query_string = ''
    if sort_by:
        # query_string = '& sort_by = popularity.desc'
        query_string += '&sort_by={}'.format(sort_by)
    if include_adult:
        # query_string = '& include_adult = false'
        query_string += '&include_adult={}'.format(include_adult)
    if include_video:
        # query_string = '& include_video = false'
        query_string += '&include_video={}'.format(include_video)
    if page:
        # query_string = '& page = 1'
        query_string += '&page={}'.format(page)
    if with_watch_monetization_types:
        # query_string = '& with_watch_monetization_types = flatrate'
        query_string += '&with_watch_monetization_types={}'.format(with_watch_monetization_types)
    if language:
        # query_string = 'language = en - US'
        query_string += '&language={}'.format(language)
    return 'https://api.themoviedb.org/3/discover/movie?api_key={}' + query_string


def get_discover_tv_url(language=None, sort_by=None, air_date_gte=None, air_date_lte=None, first_air_date_gte=None,
                        first_air_date_lte=None, first_air_date_year=None, page=None, vote_average_gte=None,
                        vote_count_gte=None, with_genres=None, without_genres=None, with_runtime_gte=None,
                        with_runtime_lte=None, with_original_language=None, with_watch_monetization_types=None):
    query_string = ''
    if language:
        query_string += '&language={}'.format(language)
    if sort_by:
        query_string += '&sort_by={}'.format(sort_by)
    if air_date_gte:
        query_string += '&air_date.gte={}'.format(air_date_gte)
    if air_date_lte:
        query_string += '&air_date.lte={}'.format(air_date_lte)
    if first_air_date_gte:
        query_string += '&first_air_date.gte={}'.format(first_air_date_gte)
    if first_air_date_lte:
        query_string += '&first_air_date.lte={}'.format(first_air_date_lte)
    if first_air_date_year:
        query_string += '&first_air_date_year={}'.format(first_air_date_year)
    if page:
        query_string += '&page={}'.format(page)
    if vote_average_gte:
        query_string += '&vote_average.gte={}'.format(vote_average_gte)
    if vote_count_gte:
        query_string += '&vote_count.gte={}'.format(vote_count_gte)
    if with_genres:
        query_string += '&with_genres={}'.format(with_genres)
    if without_genres:
        query_string += '&without_genres={}'.format(without_genres)
    if with_runtime_gte:
        query_string += '&with_runtime.gte={}'.format(with_runtime_gte)
    if with_runtime_lte:
        query_string += '&with_runtime.lte={}'.format(with_runtime_lte)
    if with_original_language:
        query_string += '&with_original_language={}'.format(with_original_language)
    if with_watch_monetization_types:
        query_string += '&with_watch_monetization_types={}'.format(with_watch_monetization_types)
    return 'https://api.themoviedb.org/3/discover/tv?api_key={}' + query_string


def make_tmdb_get_request(url):
    url = url.format(Config.AUTH_V3.API_KEY_V3_AUTH)
    response = requests.get(url, verify=True)
    if response.status_code in (200, 201):
        response_json = response.json()
        print('response_json:', response_json)
        return response_json
    else:
        print('response_json:', response.content)
        return response.status_code

# TODO: add endpoints from TV api