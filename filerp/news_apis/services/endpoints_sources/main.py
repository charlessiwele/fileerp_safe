from news_apis.services.config import Config


class EndpointsSources:
    url = 'https://newsapi.org/v2/sources?apiKey=API_KEY'

    @staticmethod
    def get_sources_by_business():
        return f'https://newsapi.org/v2/sources?category={SourceCategories.business}&apiKey=API_KEY'

    @staticmethod
    def get_sources_by_science():
        return f'https://newsapi.org/v2/sources?category={SourceCategories.science}&apiKey={Config.API_KEY}'

    @staticmethod
    def get_sources_by_sports():
        return f'https://newsapi.org/v2/sources?category={SourceCategories.sports}&apiKey={Config.API_KEY}'

    @staticmethod
    def get_sources_by_health():
        return f'https://newsapi.org/v2/sources?category={SourceCategories.health}&apiKey={Config.API_KEY}'

    @staticmethod
    def get_sources_by_general():
        return f'https://newsapi.org/v2/sources?category={SourceCategories.general}&apiKey={Config.API_KEY}'

    @staticmethod
    def get_sources_by_entertainment():
        return f'https://newsapi.org/v2/sources?category={SourceCategories.entertainment}&apiKey={Config.API_KEY}'

    @staticmethod
    def get_sources_by_technology():
        return f'https://newsapi.org/v2/sources?category={SourceCategories.technology}&apiKey={Config.API_KEY}'

    @staticmethod
    def get_sources_by_country(country):
        return f'https://newsapi.org/v2/sources?country={country}&apiKey={Config.API_KEY}'

    @staticmethod
    def get_sources_by_country_category(country, category):
        return f'https://newsapi.org/v2/sources?category={category}&country={country}&apiKey={Config.API_KEY}'


class SourceCountries:
    ae = 'ae'
    ar = 'ar'
    at = 'at'
    au = 'au'
    be = 'be'
    bg = 'bg'
    br = 'br'
    ca = 'ca'
    ch = 'ch'
    cn = 'cn'
    co = 'co'
    cu = 'cu'
    cz = 'cz'
    de = 'de'
    eg = 'eg'
    fr = 'fr'
    gb = 'gb'
    gr = 'gr'
    hk = 'hk'
    hu = 'hu'
    id = 'id'
    ie = 'ie'
    il = 'il'
    in_ = 'in'
    it = 'it'
    jp = 'jp'
    kr = 'kr'
    lt = 'lt'
    lv = 'lv'
    ma = 'ma'
    mx = 'mx'
    my = 'my'
    ng = 'ng'
    nl = 'nl'
    no = 'no'
    nz = 'nz'
    ph = 'ph'
    pl = 'pl'
    pt = 'pt'
    ro = 'ro'
    rs = 'rs'
    ru = 'ru'
    sa = 'sa'
    se = 'se'
    sg = 'sg'
    si = 'si'
    sk = 'sk'
    th = 'th'
    tr = 'tr'
    tw = 'tw'
    ua = 'ua'
    us = 'us'
    ve = 've'
    za = 'za'


class SourceCategories:
    business = 'business'
    entertainment = 'entertainment'
    general = 'general'
    health = 'health'
    science = 'science'
    sports = 'sports'
    technology = 'technology'
