from eccommerce_solutions.services.woo_commerce import WooCommerceService


class WooCommerceProductServices(WooCommerceService):

    def get_all_products(self, next_page=None):
        if next_page:
            response = self.woo_commerce_api_connection.get(f'products?{next_page}')
        else:
            response = self.woo_commerce_api_connection.get('products')

        next_page_link = response.links.get('next')
        next_page = None
        if next_page_link:
            next_page_url = next_page_link.get('url')
            start_index = str(next_page_url).find('page')
            next_page = next_page_url[start_index:]

        return {
            'next_page': next_page,
            'products': response.json()
        }

    def get_detail_product(self, product_id):
        result = self.woo_commerce_api_connection.get(f'products/{product_id}').json()
        return result

    def update_product_field(self, product_id, key_value_pair: dict):
        result = self.woo_commerce_api_connection.put(f'products/{product_id}', key_value_pair).json()
        return result

    def delete_product(self, product_id):
        result = self.woo_commerce_api_connection.delete(f'products/{product_id}', params={"force": True}).json()
        return result

    def create_product(self, name, product_type, regular_price, description, short_description, category_id, src):
        data = {
            "name": name,
            "type": product_type,
            "regular_price": regular_price,
            "description": description,
            "short_description": short_description,
            "categories": [{"id": category_id}],
            "images": [{"src": src}]
        }
        return self.woo_commerce_api_connection.post("products", data).json()

    def batch_create_products(self, product_list):
        data = {
            "create": product_list
        }
        return self.woo_commerce_api_connection.post("products/batch", data).json()

    def batch_delete_products(self, product_id_list):
        data = {
            "delete": product_id_list
        }
        return self.woo_commerce_api_connection.post("products/batch", data).json()

    def batch_update_product(self):
        # TODO:http://woocommerce.github.io/woocommerce-rest-api-docs/?python#batch-update-products
        pass
