import logging

from django.core.management import BaseCommand

from eccommerce_solutions.models import WooCommerceProductCategory, WooCommerceProduct, WooCommerceProductTag, \
    WooCommerceProductImage, WooCommerceProductCategoryImage, WooCommerceTaggedProduct, WooCommerceCustomer, \
    WooCommerceBillingAddress, WooCommerceOrder, WooCommerceShippingAddress, WooCommerceCategorisedProduct
from eccommerce_solutions.services.woo_commerce.customer_services import WooCommerceCustomerServices
from eccommerce_solutions.services.woo_commerce.order_services import WooCommerceOrderServices
from eccommerce_solutions.services.woo_commerce.product_category_services import WooCommerceProductCategoryServices
from eccommerce_solutions.services.woo_commerce.product_services import WooCommerceProductServices
from eccommerce_solutions.services.woo_commerce.product_tag_services import WooCommerceProductTagServices
from eccommerce_solutions.models import AddressFields

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Import and sync shop data from WooCommerce'

    @staticmethod
    def handle_orders_sync():
        logger.info('handle_orders_sync start')
        result = WooCommerceOrderServices().get_all_orders()
        next_page = result.get('next_page')
        woo_orders = result.get('orders')

        while woo_orders:
            for woo_order in woo_orders:

                woo_commerce_customer_id = woo_order.get('customer_id') or woo_order.get('email')
                customer, created = WooCommerceCustomer.objects.get_or_create(
                    woo_commerce_customer_id=woo_commerce_customer_id)
                order, created = WooCommerceOrder.objects.get_or_create(
                    woo_commerce_order_id=woo_order.get('id'))

                order.customer_id = customer.woo_commerce_customer_id
                order.customer_note = woo_order.get('customer_note')
                order.payment_method = woo_order.get('payment_method')
                order.payment_method_title = woo_order.get('payment_method_title')
                order.set_paid = woo_order.get('set_paid')
                order.order_number = woo_order.get('order_number')
                order.status = woo_order.get('status')
                order.date_modified = woo_order.get('date_modified')
                order.discount_total = woo_order.get('discount_total')
                order.discount_tax = woo_order.get('discount_tax')
                order.shipping_total = woo_order.get('shipping_total')
                order.shipping_tax = woo_order.get('shipping_tax')
                order.total = woo_order.get('total')
                order.customer_id = woo_order.get('customer_id')
                order.date_paid = woo_order.get('date_paid')

                billing = AddressFields()
                billing.set_address_fields_from_dict(woo_order.get('billing'))

                billing_address, created = WooCommerceBillingAddress.objects.get_or_create(
                    woo_commerce_customer_id=billing.customer_id,
                    first_name=billing.first_name,
                    last_name=billing.last_name,
                    company=billing.company,
                    address_1=billing.address_1,
                    address_2=billing.address_2,
                    email=billing.email,
                    phone=billing.phone
                )
                order.billing = billing_address

                shipping = AddressFields()
                shipping.set_address_fields_from_dict(woo_order.get('shipping'))

                shipping_address, created = WooCommerceShippingAddress.objects.get_or_create(
                    woo_commerce_customer_id=shipping.customer_id,
                    first_name=shipping.first_name,
                    last_name=shipping.last_name,
                    company=shipping.company,
                    address_1=shipping.address_1,
                    address_2=shipping.address_2,
                    email=shipping.email,
                    phone=shipping.phone
                )
                order.shipping = shipping_address

                order.line_items = str(woo_order.get('line_items'))
                order.shipping_lines = str(woo_order.get('shipping_lines'))

                order.save()
            woo_orders = None
            if next_page:
                logger.info('fetching more orders...')
                result = WooCommerceOrderServices().get_all_orders(next_page)
                next_page = result.get('next_page')
                woo_orders = result.get('orders')
        logger.info('handle_orders_sync end')

    @staticmethod
    def handle_product_tags_sync():
        logger.info('handle_product_tags_sync start')
        result = WooCommerceProductTagServices().get_all_product_tags()
        next_page = result.get('next_page')
        woo_product_tags = result.get('tags')

        while woo_product_tags:
            for woo_product_tag in woo_product_tags:
                tag, created = WooCommerceProductTag.objects.get_or_create(
                    woo_commerce_product_tag_id=woo_product_tag.get('id'))
                tag.name = woo_product_tag.get('name')
                tag.slug = woo_product_tag.get('slug')
                tag.description = woo_product_tag.get('description')
                tag.count = woo_product_tag.get('count')
                tag.save()
            woo_product_tags = None
            if next_page:
                logger.info('fetching more tags...')
                result = WooCommerceProductTagServices().get_all_product_tags(next_page)
                next_page = result.get('next_page')
                woo_product_tags = result.get('tags')
        logger.info('handle_product_tags_sync end')

    @staticmethod
    def handle_customer_sync():
        logger.info('handle_customer_sync start')
        result = WooCommerceCustomerServices().get_all_customers()
        next_page = result.get('next_page')
        woo_customers = result.get('customers')

        while woo_customers:
            for woo_customer in woo_customers:
                customer, created = WooCommerceCustomer.objects.get_or_create(
                    woo_commerce_customer_id=woo_customer.get('id'))

                customer.email = woo_customer.get('email')
                customer.first_name = woo_customer.get('first_name')
                customer.last_name = woo_customer.get('last_name')
                customer.username = woo_customer.get('username')

                customer.billing_address_first_name = woo_customer.get('billing').get('first_name')
                customer.billing_address_last_name = woo_customer.get('billing').get('last_name')
                customer.billing_address_company = woo_customer.get('billing').get('company')
                customer.billing_address_address_1 = woo_customer.get('billing').get('address_1')
                customer.billing_address_address_2 = woo_customer.get('billing').get('address_2')
                customer.billing_address_city = woo_customer.get('billing').get('city')
                customer.billing_address_state = woo_customer.get('billing').get('state')
                customer.billing_address_postcode = woo_customer.get('billing').get('postcode')
                customer.billing_address_country = woo_customer.get('billing').get('country')
                customer.billing_address_email = woo_customer.get('billing').get('email')
                customer.billing_address_phone = woo_customer.get('billing').get('phone')

                customer.shipping_address_first_name = woo_customer.get('shipping').get('first_name')
                customer.shipping_address_last_name = woo_customer.get('shipping').get('last_name')
                customer.shipping_address_company = woo_customer.get('shipping').get('company')
                customer.shipping_address_address_1 = woo_customer.get('shipping').get('address_1')
                customer.shipping_address_address_2 = woo_customer.get('shipping').get('address_2')
                customer.shipping_address_city = woo_customer.get('shipping').get('city')
                customer.shipping_address_state = woo_customer.get('shipping').get('state')
                customer.shipping_address_postcode = woo_customer.get('shipping').get('postcode')
                customer.shipping_address_country = woo_customer.get('shipping').get('country')
                customer.shipping_address_email = woo_customer.get('shipping').get('email')
                customer.shipping_address_phone = woo_customer.get('shipping').get('phone')
                customer.save()

            woo_customers = None
            if next_page:
                result = WooCommerceCustomerServices().get_all_customers(next_page)
                logger.info('fetching more customers...')
                next_page = result.get('next_page')
                woo_customers = result.get('customers')
        logger.info('handle_customer_sync end')

    @staticmethod
    def handle_product_category_sync():
        logger.info('handle_customer_sync start')
        result = WooCommerceProductCategoryServices().get_all_product_categories()
        next_page = result.get('next_page')
        woo_product_categories = result.get('categories')
        while woo_product_categories:
            for woo_product_category in woo_product_categories:
                woo_product_image = None

                if woo_product_category.get('image'):
                    woo_product_image, created = WooCommerceProductCategoryImage.objects.get_or_create(
                        woo_commerce_product_image_id=woo_product_category.get('image').get('id')
                    )
                    woo_product_image.src=woo_product_category.get('image').get('src')
                    woo_product_image.name=woo_product_category.get('image').get('name')
                    woo_product_image.alt=woo_product_category.get('image').get('alt')
                    woo_product_image.save()

                product_category, created = WooCommerceProductCategory.objects.get_or_create(
                    woo_commerce_product_category_id=woo_product_category.get('id'))
                product_category.name = woo_product_category.get('name')
                product_category.slug = woo_product_category.get('slug')
                product_category.description = woo_product_category.get('description')
                product_category.image = woo_product_image
                product_category.count = woo_product_category.get('count')
                product_category.parent = woo_product_category.get('parent')
                product_category.save()
            woo_product_categories = None
            if next_page:
                logger.info('fetching more categories...')
                result = WooCommerceProductCategoryServices().get_all_product_categories(next_page)
                next_page = result.get('next_page')
                woo_product_categories = result.get('categories')
        logger.info('handle_customer_sync end')

    @staticmethod
    def handle_product_sync():
        logger.info('handle_product_sync start')
        result = WooCommerceProductServices().get_all_products()
        next_page = result.get('next_page')
        woo_products = result.get('products')

        while woo_products:
            for woo_product in woo_products:
                product, created = WooCommerceProduct.objects.get_or_create(
                    woo_commerce_product_id=woo_product.get('id')
                )

                for woo_product_image in woo_product.get('images'):
                    woo_commerce_product_image, created = WooCommerceProductImage.objects.get_or_create(
                        woo_commerce_product_image_id=woo_product_image.get('id'),
                        woo_commerce_product=product
                    )
                    woo_commerce_product_image.src = woo_product_image.get('src')
                    woo_commerce_product_image.name = woo_product_image.get('name')
                    woo_commerce_product_image.alt = woo_product_image.get('alt')
                    woo_commerce_product_image.save()

                for woo_product_tag in woo_product.get('tags'):
                    product_tag, created = WooCommerceProductTag.objects.get_or_create(
                        woo_commerce_product_tag_id=woo_product_tag.get('id')
                    )
                    WooCommerceTaggedProduct.objects.get_or_create(
                        woo_commerce_tag=product_tag,
                        woo_commerce_product=product
                    )

                product.related_ids = woo_product.get('related_ids')
                product.grouped_products = woo_product.get('grouped_products')
                product.parent_id = woo_product.get('parent_id')
                product.name = woo_product.get('name')
                product.slug = woo_product.get('slug')
                product.permalink = woo_product.get('permalink')
                product.type = woo_product.get('type')
                product.status = woo_product.get('status')
                product.featured = woo_product.get('featured')
                product.description = woo_product.get('description')
                product.short_description = woo_product.get('short_description')
                product.sku = woo_product.get('sku')
                product.price = woo_product.get('price')
                product.regular_price = woo_product.get('regular_price')
                product.sale_price = woo_product.get('sale_price')
                product.price_html = woo_product.get('price_html')
                product.on_sale = woo_product.get('on_sale')
                product.purchasable = woo_product.get('purchasable')
                product.total_sales = woo_product.get('total_sales')
                product.stock_quantity = woo_product.get('stock_quantity')
                product.stock_status = woo_product.get('stock_status')
                product.average_rating = woo_product.get('average_rating')
                product.rating_count = woo_product.get('rating_count')
                product.save()

                logger.info('product categorization start: {}'.format(product.name))
                woo_commerce_product_categories = woo_product.get('categories')
                for woo_commerce_product_category in woo_commerce_product_categories:
                    product_category, created = WooCommerceProductCategory.objects.get_or_create(
                        woo_commerce_product_category_id=woo_commerce_product_category.get('id'),
                        name=woo_commerce_product_category.get('name'),
                        slug=woo_commerce_product_category.get('slug')
                    )
                    WooCommerceCategorisedProduct.objects.get_or_create(
                        woo_commerce_product_category=product_category,
                        woo_commerce_product=product
                    )
                logger.info('products categorization end')

            woo_products = None
            if next_page:
                logger.info('fetching more products...')

                result = WooCommerceProductServices().get_all_products(next_page)
                next_page = result.get('next_page')
                woo_products = result.get('products')
        logger.info('handle_product_sync end')

    def handle(self, *args, **options):
        self.handle_product_tags_sync()
        self.handle_product_category_sync()
        self.handle_product_sync()
        self.handle_customer_sync()
        self.handle_orders_sync()
