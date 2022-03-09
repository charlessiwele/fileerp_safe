import datetime
from django.contrib import admin
from django.template.loader import render_to_string
from data_center import models


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_1', 'address_2', 'city', 'state', 'postcode', 'country']
    search_fields = ['address_1', 'address_2', 'city', 'state', 'postcode', 'country']
    list_filter = ['city', 'state', 'country']


@admin.register(models.CustomerType)
class CustomerTypeAdmin(admin.ModelAdmin):
    list_display = ['customer_type_name']


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_type', 'image_display']
    list_filter = ['customer_type']
    search_fields = ['customer_name']

    @staticmethod
    def image_display(obj):
        return render_to_string('render/basic_image_display.html', {'image_url': obj.image})


@admin.register(models.StaffType)
class StaffTypeAdmin(admin.ModelAdmin):
    list_display = ['staff_type_name']


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['staff_name', 'staff_type', 'image']
    list_filter = ['staff_type']
    search_fields = ['staff_name']


@admin.register(models.ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['product_type_name']
    search_fields = ['product_type_name']


@admin.register(models.ProductVariation)
class ProductVariationAdmin(admin.ModelAdmin):
    list_display = ['product_variation_name', 'product_variation_code']
    search_fields = ['product_variation_name', 'product_variation_code']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_code', 'product_name', 'product_type', 'product_variation', 'product_price']
    list_filter = ['product_type']
    search_fields = ['product_code', 'product_name', 'product_type', 'product_price']


@admin.register(models.InvoiceProduct)
class InvoiceProductAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'product', 'product_quantity']


class InvoiceProductTabularInline(admin.TabularInline):
    model = models.InvoiceProduct


class QuotationProductTabularInline(admin.TabularInline):
    model = models.QuotationProduct


@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_no', 'customer']
    search_fields = ['invoice_no']
    inlines = [InvoiceProductTabularInline]
    autocomplete_fields = ['customer']
    change_form_template = 'admin/invoices_change_form.html'

    def get_form(self, request, obj=None, **kwargs):
        form = super(InvoiceAdmin, self).get_form(request, obj, **kwargs)
        datetime_now = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        if not obj:
            form.base_fields['invoice_no'].initial = f'INV_{datetime_now}'
        return form

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if obj and obj.pk:
            context['pk'] = obj.pk
        return super(InvoiceAdmin, self).render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)


@admin.register(models.Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ['quote_no', 'customer']
    search_fields = ['quote_no']
    inlines = [QuotationProductTabularInline]
    autocomplete_fields = ['customer']
    change_form_template = 'admin/quotations_change_form.html'

    def get_form(self, request, obj=None, **kwargs):
        form = super(QuotationAdmin, self).get_form(request, obj, **kwargs)
        datetime_now = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        if not obj:
            form.base_fields['quote_no'].initial = f'QUOTE_{datetime_now}'
        return form

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if obj and obj.pk:
            context['pk'] = obj.pk
        return super(QuotationAdmin, self).render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)
