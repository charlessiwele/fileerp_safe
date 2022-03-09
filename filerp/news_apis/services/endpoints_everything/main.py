from datetime import datetime

from news_apis.services.config import Config


class Keywords:
# params:
# q: Keywords or phrases to search for in the article title and body.
# Advanced search is supported here:

    def __init__(self):
        self.q_exact_match = ''
        self.q_must_match_have = ''
        self.q_must_not_match_have = ''

    # Surround phrases with quotes (") for exact match.
    def build_q_exact_match(self, q_exact_match):
        self.q_exact_match = "q='{}'".format(q_exact_match)

    # Prepend words or phrases that must appear with a + symbol. Eg: +bitcoin
    def build_q_must_match_have(self, q_must_match_have):
        self.q_must_match_have = "q=+{}".format(q_must_match_have)

    # Prepend words that must not appear with a - symbol. Eg: -bitcoin
    def build_q_must_not_match_have(self, q_must_not_match_have):
        self.q_must_not_match_have = "q=-{}".format(q_must_not_match_have)


    # Alternatively you can use the AND / OR / NOT keywords, and optionally group these with parenthesis. Eg: crypto AND (ethereum OR litecoin) NOT bitcoin.
    # The complete value for q must be URL-encoded
    def get_q_keyword(self):
        query_string = ''
        if self.q_must_not_match_have:
            query_string += f'{self.q_must_not_match_have}&'
        if self.q_must_match_have:
            query_string += f'{self.q_must_match_have}&'
        if self.q_exact_match:
            query_string += f'{self.q_exact_match}&'
        return query_string


class KeywordsInArticleTitle:
    # params:
    # qInTitle: Keywords or phrases to search for in the article title only.
    # Surround phrases with quotes (") for exact match.
    # Surround phrases with quotes (") for exact match.

    def __init__(self):
        self.q_exact_match = ''
        self.q_must_match_have = ''
        self.q_must_not_match_have = ''


    # Surround phrases with quotes (") for exact match.
    def build_q_in_title_exact_match(self, q_exact_match):
        return "q='{}'".format(q_exact_match)


    # Prepend words or phrases that must appear with a + symbol. Eg: +bitcoin
    def build_q_in_title_must_match_have(self, q_must_match_have):
        return "q=+{}".format(q_must_match_have)


    # Prepend words that must not appear with a - symbol. Eg: -bitcoin
    def build_q_in_title_must_not_match_have(self, q_must_not_match_have):
        return "q=-{}".format(q_must_not_match_have)


    # The complete value for q must be URL-encoded
    def get_q_in_title(self, q_exact_match = None, q_must_match_have = None, q_must_not_match_have = None):
        query_string =''
        if q_must_not_match_have:
            query_string += q_must_not_match_have + '&'
        if q_must_match_have:
            query_string += q_must_match_have + '&'
        if q_exact_match:
            query_string += q_exact_match + '&'
        return query_string


# params:
# endpoints_sources: A comma-seperated string of identifiers (maximum 20) for the news endpoints_sources or blogs you want headlines from.
# Use the /endpoints_sources endpoint to locate these programmatically or look at the endpoints_sources index.
def get_sources_endpoint():
    return '/endpoints_sources'


# language
# The 2-letter ISO-639-1 code of the language you want to get headlines for. Possible options:
class Language:
    ar = 'ar'
    de = 'de'
    en = 'en'
    es = 'es'
    fr = 'fr'
    he = 'he'
    it = 'it'
    nl = 'nl'
    no = 'no'
    pt = 'pt'
    ru = 'ru'
    se = 'se'
    ud = 'ud'
    zh = 'zh'


# sortBy
# The order to sort the articles in. Possible options: relevancy, popularity, publishedAt.
# relevancy = articles more closely related to q come first.
# popularity = articles from popular endpoints_sources and publishers come first.
# publishedAt = newest articles come first.
class SortBy:
    relevancy = 'relevancy'
    popularity = 'popularity'
    publishedAt = 'publishedAt'


class EndpointsEverything:

    @staticmethod
    def with_keyword(with_keyword, page_size=50):
        keywords_class = Keywords()
        keywords_class.build_q_exact_match(with_keyword)
        keyword = keywords_class.get_q_keyword()
        return f'https://newsapi.org/v2/everything?{keyword}apiKey={Config.API_KEY}&pageSize={page_size}'

    @staticmethod
    def with_keyword_from_date(with_keyword, from_date: datetime = datetime.now(), page_size=50):

        from_date = from_date.strftime('%Y-%m-%d')

        keywords_class = Keywords()
        keywords_class.build_q_exact_match(with_keyword)
        keyword = keywords_class.get_q_keyword()
        return f'https://newsapi.org/v2/everything?{keyword}from={from_date}&apiKey={Config.API_KEY}&pageSize={page_size}'

    @staticmethod
    def with_keyword_from_date_to_date(with_keyword, from_date: datetime = datetime.now(),
                                       to_date: datetime = datetime.now(), page_size=50):

        from_date = from_date.strftime('%Y-%m-%d')
        to_date = to_date.strftime('%Y-%m-%d')

        keywords_class = Keywords()
        keywords_class.build_q_exact_match(with_keyword)
        keyword = keywords_class.get_q_keyword()
        return f'https://newsapi.org/v2/everything?{keyword}from={from_date}&to={to_date}&apiKey={Config.API_KEY}&pageSize={page_size}'

    @staticmethod
    def with_keyword_domains(with_keyword, domains, page_size=50):

        keywords_class = Keywords()
        keywords_class.build_q_exact_match(with_keyword)
        keyword = keywords_class.get_q_keyword()
        return f'https://newsapi.org/v2/everything?{keyword}domains={domains}&apiKey={Config.API_KEY}&pageSize={page_size}'

