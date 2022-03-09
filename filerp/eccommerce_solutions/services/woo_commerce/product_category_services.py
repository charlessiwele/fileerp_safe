from eccommerce_solutions.services.woo_commerce import WooCommerceService


class WooCommerceProductCategoryServices(WooCommerceService):

    def get_all_product_categories(self, next_page: str = None):
        if next_page:
            response = self.woo_commerce_api_connection.get(f'products/categories?{next_page}')
        else:
            response = self.woo_commerce_api_connection.get('products/categories')

        next_page_link = response.links.get('next')
        next_page = None
        if next_page_link:
            next_page_url = next_page_link.get('url')
            start_index = str(next_page_url).find('page')
            next_page = next_page_url[start_index:]

        return {
            'next_page': next_page,
            'categories': response.json()
        }

    def get_detail_product_category(self, product_category_id):
        result = self.woo_commerce_api_connection.get(f'products/categories/{product_category_id}').json()
        return result

    def update_product_category_field(self, product_category_id, key_value_pair: dict):
        result = self.woo_commerce_api_connection.put(f'products/categories/{product_category_id}', key_value_pair).json()
        return result

    def delete_product_category(self, product_category_id):
        result = self.woo_commerce_api_connection.delete(f'products/categories/{product_category_id}', params={"force": True}).json()
        return result

    def create_product_category(self, name, slug, description, image_src):
        data = {
            "name": name,
            "slug": slug,
            "description": description,
            "image": {
                "src": image_src
            }
        }
        return self.woo_commerce_api_connection.post("products/categories", data).json()

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

