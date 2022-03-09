from django.db import models


# Create your models here.
class ModelAbstractCityPostcodeStateCountry(models.Model):
    postcode = models.CharField(max_length=5, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        abstract = True


class ModelAbstractAddressType(models.Model):
    is_billing = models.BooleanField(blank=True, null=True)
    is_shipping = models.BooleanField(blank=True, null=True)

    class Meta:
        abstract = True


class ModelAbstractAddress(ModelAbstractCityPostcodeStateCountry):
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    company = models.CharField(max_length=500, blank=True, null=True)
    address_1 = models.CharField(max_length=500, blank=True, null=True)
    address_2 = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    # postcode, city, country, state inherited from ModelAbstractCityPostcodeCountry

    class Meta:
        abstract = True


class WooCommerceProductCategoryImage(models.Model):
    woo_commerce_product_image_id = models.CharField(max_length=20, blank=True, null=True)
    src = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    alt = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        if self.name:
            return str(self.name) + '-' + str(self.src)
        elif self.alt:
            return str(self.alt) + '-' + str(self.src)
        return self.src


class WooCommerceProductCategory(models.Model):
    woo_commerce_product_category_id = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    slug = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ForeignKey(WooCommerceProductCategoryImage, on_delete=models.SET_NULL, blank=True, null=True)
    parent = models.CharField(max_length=20, blank=True, null=True)
    count = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name_plural = "WooCommerce Product Categories"

    def __str__(self):
        return self.name


class WooCommerceProductTag(models.Model):
    woo_commerce_product_tag_id = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    slug = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    count = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "WooCommerce Product Tags"

    def __str__(self):
        return self.name


class WooCommerceProduct(models.Model):
    woo_commerce_product_id = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    slug = models.CharField(max_length=500, blank=True, null=True)
    permalink = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=500, blank=True, null=True)
    featured = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    short_description = models.CharField(max_length=500, blank=True, null=True)
    sku = models.CharField(max_length=500, blank=True, null=True)
    price = models.CharField(max_length=500, blank=True, null=True)
    regular_price = models.CharField(max_length=500, blank=True, null=True)
    sale_price = models.CharField(max_length=500, blank=True, null=True)
    price_html = models.CharField(max_length=500, blank=True, null=True)
    on_sale = models.CharField(max_length=500, blank=True, null=True)
    purchasable = models.CharField(max_length=500, blank=True, null=True)
    total_sales = models.CharField(max_length=500, blank=True, null=True)
    stock_quantity = models.CharField(max_length=500, blank=True, null=True)
    stock_status = models.CharField(max_length=500, blank=True, null=True)
    average_rating = models.CharField(max_length=500, blank=True, null=True)
    rating_count = models.CharField(max_length=500, blank=True, null=True)
    related_ids = models.CharField(max_length=500, blank=True, null=True)
    grouped_products = models.CharField(max_length=500, blank=True, null=True)
    parent_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name_plural = "WooCommerce Products"

    def __str__(self):
        return self.name


class WooCommerceProductImage(models.Model):
    woo_commerce_product_image_id = models.CharField(max_length=20, blank=True, null=True)
    src = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    alt = models.CharField(max_length=500, blank=True, null=True)
    woo_commerce_product = models.ForeignKey(WooCommerceProduct, on_delete=models.CASCADE, blank=True, null=True)


class WooCommerceTaggedProduct(models.Model):
    woo_commerce_tag = models.ForeignKey(WooCommerceProductTag, on_delete=models.CASCADE)
    woo_commerce_product = models.ForeignKey(WooCommerceProduct, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "WooCommerce Tagged Products"

    def __str__(self):
        display_name = f'{self.woo_commerce_tag.slug}-{self.woo_commerce_product.slug}'
        return display_name


class WooCommerceCategorisedProduct(models.Model):
    woo_commerce_product_category = models.ForeignKey(WooCommerceProductCategory, on_delete=models.CASCADE)
    woo_commerce_product = models.ForeignKey(WooCommerceProduct, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "WooCommerce Categorised Products"
        unique_together = ['woo_commerce_product_category', 'woo_commerce_product']

    def __str__(self):
        return str(self.woo_commerce_product.slug) + str(self.woo_commerce_product_category.slug)


class WooCommerceCustomer(models.Model):
    woo_commerce_customer_id = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name_plural = "WooCommerce Customers"

    def __str__(self):
        return self.username


class WooCommerceBillingAddress(ModelAbstractAddress):
    woo_commerce_customer_id = models.ForeignKey(
        WooCommerceCustomer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        unique=True
    )


class WooCommerceShippingAddress(ModelAbstractAddress):
    woo_commerce_customer_id = models.ForeignKey(
        WooCommerceCustomer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        unique=True
    )


class WooCommerceOrder(models.Model):
    woo_commerce_order_id = models.CharField(max_length=500, blank=True, null=True)
    order_number = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=500, blank=True, null=True)
    date_modified = models.CharField(max_length=500, blank=True, null=True)
    discount_total = models.CharField(max_length=500, blank=True, null=True)
    discount_tax = models.CharField(max_length=500, blank=True, null=True)
    shipping_total = models.CharField(max_length=500, blank=True, null=True)
    shipping_tax = models.CharField(max_length=500, blank=True, null=True)
    total = models.CharField(max_length=500, blank=True, null=True)
    customer_id = models.CharField(max_length=500, blank=True, null=True)
    date_paid = models.CharField(max_length=500, blank=True, null=True)
    customer_note = models.CharField(max_length=500, blank=True, null=True)
    payment_method = models.CharField(max_length=500, blank=True, null=True)
    payment_method_title = models.CharField(max_length=500, blank=True, null=True)
    set_paid = models.CharField(max_length=15, blank=True, null=True)
    shipping_lines = models.CharField(max_length=500, blank=True, null=True)
    line_items = models.CharField(max_length=500, blank=True, null=True)

    woo_commerce_customer = models.ForeignKey(
        WooCommerceCustomer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    woo_commerce_billing_address = models.ForeignKey(
        WooCommerceBillingAddress,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    woo_commerce_shipping_address = models.ForeignKey(
        WooCommerceShippingAddress,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class AddressFields:
    def __init__(self, first_name=None, last_name=None, company=None, address_1=None, address_2=None,
                 city=None, state=None, postcode=None, country=None, email=None, phone=None, customer_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.postcode = postcode
        self.country = country
        self.email = email
        self.phone = phone
        self.customer_id = customer_id

    def get_address_fields_as_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'company': self.company,
            'address_1': self.address_1,
            'address_2': self.address_2,
            'city': self.city,
            'state': self.state,
            'postcode': self.postcode,
            'country': self.country,
            'email': self.email,
            'phone': self.phone
        }
