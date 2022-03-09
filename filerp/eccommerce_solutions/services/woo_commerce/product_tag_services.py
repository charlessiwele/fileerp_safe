from eccommerce_solutions.services.woo_commerce import WooCommerceService


class WooCommerceProductTagServices(WooCommerceService):

    def get_all_product_tags(self, next_page: str = None):
        if next_page:
            response = self.woo_commerce_api_connection.get(f'products/tags?{next_page}')
        else:
            response = self.woo_commerce_api_connection.get('products/tags')

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

    def get_detail_product_tag(self, product_tag_id):
        result = self.woo_commerce_api_connection.get(f'products/tags/{product_tag_id}').json()
        return result

    def update_product_tag_field(self, product_tag_id, key_value_pair: dict):
        result = self.woo_commerce_api_connection.put(f'products/tags/{product_tag_id}', key_value_pair).json()
        return result

    def delete_product_category(self, product_tag_id):
        result = self.woo_commerce_api_connection.delete(f'products/tags/{product_tag_id}').json()
        return result

    def create_product_tag(self, name):
        data = {
            "name": name,
        }
        return self.woo_commerce_api_connection.post("products/tags", data).json()

    def batch_create_tags(self, tag_list):
        data = {
            "create": tag_list
        }
        return self.woo_commerce_api_connection.post("products/tags/batch", data).json()

    def batch_delete_products(self, tag_id_list):
        data = {
            "delete": tag_id_list
        }
        return self.woo_commerce_api_connection.post("products/tags/batch", data).json()

