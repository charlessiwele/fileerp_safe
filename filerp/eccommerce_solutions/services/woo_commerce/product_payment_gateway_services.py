from eccommerce_solutions.services.woo_commerce import WooCommerceService


class WooCommercePaymentGatewayServices(WooCommerceService):

    def get_all_payment_gateways(self, next_page: str = None):
        if next_page:
            response = self.woo_commerce_api_connection.get(f'payment_gateways?{next_page}')
        else:
            response = self.woo_commerce_api_connection.get('payment_gateways')

        next_page_link = response.links.get('next')
        next_page = None
        if next_page_link:
            next_page_url = next_page_link.get('url')
            start_index = str(next_page_url).find('page')
            next_page = next_page_url[start_index:]

        return {
            'next_page': next_page,
            'tags': response.json()
        }

    def get_detail_product_tag(self, payment_gateway_id):
        result = self.woo_commerce_api_connection.get(f'payment_gateways/{payment_gateway_id}').json()
        return result
