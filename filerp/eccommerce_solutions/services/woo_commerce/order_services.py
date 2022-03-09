from eccommerce_solutions.services.woo_commerce import WooCommerceService


class WooCommerceOrderServices(WooCommerceService):

    def get_all_orders(self, next_page: str = None):
        if next_page:
            response = self.woo_commerce_api_connection.get(f'orders?{next_page}')
        else:
            response = self.woo_commerce_api_connection.get('orders')

        next_page_link = response.links.get('next')
        next_page = None
        if next_page_link:
            next_page_url = next_page_link.get('url')
            start_index = str(next_page_url).find('page')
            next_page = next_page_url[start_index:]

        return {
            'next_page': next_page,
            'orders': response.json()
        }

    def get_detail_order(self, order_id):
        result = self.woo_commerce_api_connection.get(f'orders/{order_id}').json()
        return result

    def update_orders_field(self, order_id, key_value_pair: dict):
        result = self.woo_commerce_api_connection.put(f'orders/{order_id}', key_value_pair).json()
        return result

    def delete_order(self, order_id):
        result = self.woo_commerce_api_connection.delete(f'orders/{order_id}', params={"force": True}).json()
        return result

    def create_order(self, payment_method, payment_method_title, line_items, shipping_address, billing_address,
                     shipping_lines, set_paid=True, customer_id=0, currency='ZAR', customer_note=''):
        data = {
            "payment_method": payment_method,
            "payment_method_title": payment_method_title,
            "set_paid": set_paid,
            "billing": billing_address,
            "shipping": shipping_address,
            "line_items": line_items,
            "currency": currency,
            "customer_id": customer_id,
            "customer_note": customer_note,
            "shipping_lines": shipping_lines
        }
        return self.woo_commerce_api_connection.post("orders", data).json()

    def batch_create_orders(self, order_list):
        data = {
            "create": order_list
        }
        return self.woo_commerce_api_connection.post("orders", data).json()

    def batch_delete_orders(self, order_id_list):
        data = {
            "delete": order_id_list
        }
        return self.woo_commerce_api_connection.post("orders", data).json()

    def update_orders_status(self, order_id, status: str):
        result = self.update_orders_field(order_id, {'status': status})
        return result
