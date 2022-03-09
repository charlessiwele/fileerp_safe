from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
# Create your models here.
from django.utils.datetime_safe import datetime

from filerp.settings import BANK_DETAILS


class Address(models.Model):
    address_name = models.CharField(max_length=500, blank=True, null=True)
    address_1 = models.CharField(max_length=500, blank=True, null=True)
    address_2 = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    postcode = models.CharField(max_length=5, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    is_billing = models.BooleanField(blank=True, null=True)
    is_shipping = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.address_name}'


class CustomerType(models.Model):
    customer_type_name = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Customer Types"

    def __str__(self):
        return f'{self.customer_type_name}'


class Customer(models.Model):
    customer_name = models.CharField(max_length=500, blank=True, null=True)
    customer_type = models.ForeignKey(
        CustomerType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    customer_address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to='images/customers', blank=True, null=True)
    extra_notes = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return f'{self.customer_name}'


class StaffType(models.Model):
    staff_type_name = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Staff Types"

    def __str__(self):
        return f'{self.staff_type_name}'


class Staff(models.Model):
    staff_name = models.CharField(max_length=500, blank=True, null=True)
    staff_type = models.ForeignKey(
        StaffType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    staff_address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to='images/staff', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Staff"

    def __str__(self):
        return f'{self.staff_name}'


class ProductType(models.Model):
    product_type_name = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Product Types"

    def __str__(self):
        return f'{self.product_type_name}'


class ProductVariation(models.Model):
    product_variation_name = models.CharField(max_length=500, blank=True, null=True)
    product_variation_code = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Product Variations"

    def __str__(self):
        return f'{self.product_variation_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=500, blank=True, null=True)
    product_code = models.CharField(max_length=500, blank=True, null=True)
    product_price = models.CharField(max_length=500, blank=True, null=True)
    product_variation = models.ForeignKey(
        ProductVariation,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return f'{self.product_name}'


class Invoice(models.Model):
    invoice_no = models.CharField(max_length=500, blank=True, null=True)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Invoices"

    def __str__(self):
        return f'{self.invoice_no} for {self.customer}'


class Quotation(models.Model):
    quote_no = models.CharField(max_length=500, blank=True, null=True)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Quotes"

    def __str__(self):
        return f'{self.quote_no} for {self.customer}'


class InvoiceProduct(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    product_quantity = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
     )

    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_line_total(self):
        days_of_service = 1
        if self.check_out and self.check_out:
            days_of_service = 1
            if self.check_out > self.check_in:
                days_of_service = self.check_out - self.check_in
                days_of_service = days_of_service.days
        product_quantity = self.product_quantity
        product_price = self.product.product_price
        line_total = days_of_service * float(product_price) * float(product_quantity)
        return '%.2f' % line_total

    class Meta:
        verbose_name_plural = "Invoice Products"

    def __str__(self):
        return f'{self.product}'


class QuotationProduct(models.Model):
    quotation = models.ForeignKey(
        Quotation,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    product_quantity = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
     )

    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_line_total(self):
        days_of_service = 1
        if self.check_out and self.check_out:
            days_of_service = 1
            if self.check_out > self.check_in:
                days_of_service = self.check_out - self.check_in
                days_of_service = days_of_service.days
        product_quantity = self.product_quantity
        product_price = self.product.product_price
        line_total = days_of_service * float(product_price) * float(product_quantity)
        return '%.2f' % line_total

    class Meta:
        verbose_name_plural = "Invoice Product"

    def __str__(self):
        return f'{self.product}'

class CurrentBank:
    bank_name = BANK_DETAILS.get('bank_name')
    account_holder = BANK_DETAILS.get('account_holder')
    account_no = BANK_DETAILS.get('account_no')
    account_type = BANK_DETAILS.get('account_type')
