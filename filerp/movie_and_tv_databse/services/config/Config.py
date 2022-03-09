from filerp.settings import TMDB_API_ACCESS_TOKEN, TMDB_API_KEY


class Config:
    TMDB_ATTRIBUTION = "This product uses the TMDb API but is not endorsed or certified by TMDb."

    class AUTH_V3:
        API_KEY_V3_AUTH = TMDB_API_KEY

    class AUTH_V4:
        API_READ_ACCESS_TOKEN = TMDB_API_ACCESS_TOKEN

    class WatchMonetizationTypes:
        flatrate = 'flatrate'
        free = 'free'
        ads = 'ads'
        rent = 'rent'
        buy = 'buy'


    class DISCOVER_SORT_BY:
        popularity_asc = 'popularity.asc'
        release_date_asc = 'release_date.asc'
        revenue_asc = 'revenue.asc'
        primary_release_date_asc = 'primary_release_date.asc'
        original_title_asc = 'original_title.asc'
        vote_average_asc = 'vote_average.asc'
        vote_count_asc = 'vote_count.asc'

        popularity_desc = 'popularity.desc'
        release_date_desc = 'release_date.desc'
        revenue_desc = 'revenue.desc'
        primary_release_date_desc = 'primary_release_date.desc'
        original_title_desc = 'original_title.desc'
        vote_average_desc = 'vote_average.desc'
        vote_count_desc = 'vote_count.desc'