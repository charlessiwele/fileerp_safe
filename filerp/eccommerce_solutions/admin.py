from django.contrib import admin
from django.db import models as db_models
# Register your models here.
from eccommerce_solutions import models


class GenericWooCommerceAdmin(admin.ModelAdmin):
    readonly_fields = []
    # WOO COMMERCE FIELDS SHOULD ONLY BE EDITABLE BY PROCESSES
    # FIELDS SHOULD STILL BE VIEWABLE FOR ANALYSIS
    # E.G USER INVOKING SALE, OR A SYNC PROCESS UPDATING DATA
    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.WooCommerceProductCategory)
class WooCommerceProductCategoryAdmin(GenericWooCommerceAdmin):
    list_display = ['name', 'description', 'parent', 'count']


@admin.register(models.WooCommerceTaggedProduct)
class WooCommerceTaggedProductAdmin(GenericWooCommerceAdmin):
    pass


@admin.register(models.WooCommerceProductTag)
class WooCommerceProductTagAdmin(GenericWooCommerceAdmin):
    pass


@admin.register(models.WooCommerceProduct)
class WooCommerceProductAdmin(GenericWooCommerceAdmin):
    pass


@admin.register(models.WooCommerceCustomer)
class WooCommerceCustomerAdmin(GenericWooCommerceAdmin):
    list_display = [
        'id',
        'woo_commerce_customer_id',
        'email',
        'first_name',
        'last_name',
        'username'
    ]


@admin.register(models.WooCommerceOrder)
class WooCommerceOrderAdmin(GenericWooCommerceAdmin):
    list_display = [
        'woo_commerce_order_id',
        'order_number',
        'status',
        'date_modified',
        'total',
        'customer_id',
        'date_paid',
        'customer_note',
        'payment_method'
    ]


@admin.register(models.WooCommerceBillingAddress)
class WooCommerceBillingAddressAdmin(GenericWooCommerceAdmin):
    pass


@admin.register(models.WooCommerceShippingAddress)
class WooCommerceShippingAddressAdmin(GenericWooCommerceAdmin):
    pass

