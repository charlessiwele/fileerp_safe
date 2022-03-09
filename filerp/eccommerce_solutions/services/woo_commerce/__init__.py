from woocommerce import API

from filerp.settings import WOO_COMM_CONSUMER_KEY, WOO_COMM_CONSUMER_SECRET, SHOP_HOST_URL


class WooCommerceService():
    def __init__(self):
        self.woo_commerce_api_connection = API(
            url=SHOP_HOST_URL,
            consumer_key=WOO_COMM_CONSUMER_KEY,
            consumer_secret=WOO_COMM_CONSUMER_SECRET,
            version="wc/v3"
        )

    def get_api_end_points(self):
        result = self.woo_commerce_api_connection.get('').json()
        return result


