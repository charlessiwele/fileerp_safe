from eccommerce_solutions.services.woo_commerce import WooCommerceService


class WooCommerceCustomerServices(WooCommerceService):

    def get_all_customers(self, next_page: str = None):
        if next_page:
            response = self.woo_commerce_api_connection.get(f'customers?{next_page}')
        else:
            response = self.woo_commerce_api_connection.get('customers')

        next_page_link = response.links.get('next')
        next_page = None
        if next_page_link:
            next_page_url = next_page_link.get('url')
            start_index = str(next_page_url).find('page')
            next_page = next_page_url[start_index:]

        return {
            'next_page': next_page,
            'customers': response.json()
        }

    def get_detail_customer(self, customer_id):
        result = self.woo_commerce_api_connection.get(f'customers/{customer_id}').json()
        return result

    def get_customer_downloads(self, customer_id):
        result = self.woo_commerce_api_connection.get(f'customers/{customer_id}/downloads').json()
        return result

    def update_customer_field(self, customer_id, key_value_pair: dict):
        result = self.woo_commerce_api_connection.put(f'customers/{customer_id}', key_value_pair).json()
        return result

    def delete_customer(self, customer_id):
        result = self.woo_commerce_api_connection.delete(f'customers/{customer_id}', params={"force": True}).json()
        return result

    def create_customer(self, email, first_name, last_name, username, billing_address, shipping_address):
        data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "billing": {
                "first_name": billing_address.first_name,
                "last_name": billing_address.last_name,
                "company": billing_address.company,
                "address_1": billing_address.address_1,
                "address_2": billing_address.address_2,
                "city": billing_address.city,
                "state": billing_address.state,
                "postcode": billing_address.postcode,
                "country": billing_address.country,
                "email": billing_address.email,
                "phone": billing_address.phone
            },
            "shipping": {
                "first_name": shipping_address.first_name,
                "last_name": shipping_address.last_name,
                "company": shipping_address.company,
                "address_1": shipping_address.address_1,
                "address_2": shipping_address.address_2,
                "city": shipping_address.city,
                "state": shipping_address.state,
                "postcode": shipping_address.postcode,
                "country": shipping_address.country
            }
        }
        return self.woo_commerce_api_connection.post("customers", data).json()

    def batch_create_customers(self, customer_list):
        data = {
            "create": customer_list
        }
        return self.woo_commerce_api_connection.post("customers/batch", data).json()

    def batch_delete_customers(self, customer_id_list):
        data = {
            "delete": customer_id_list
        }
        return self.woo_commerce_api_connection.post("customers/batch", data).json()
