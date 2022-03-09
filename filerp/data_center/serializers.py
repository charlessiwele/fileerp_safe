from rest_framework import serializers
from data_center.models import Invoice, Quotation


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    invoice_no = serializers.CharField()
    customer_name = serializers.SerializerMethodField()
    customer_type = serializers.SerializerMethodField()
    customer_address = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_customer_name(self, obj):
        return obj.customer.customer_name

    def get_customer_type(self, obj):
        return obj.customer.customer_type.customer_type_name

    def get_customer_address(self, obj):
        return f'{obj.customer.customer_address.address_1} {obj.customer.customer_address.address_2}'

    def get_image(self, obj):
        return obj.customer.image.url

    class Meta:
        model = Invoice
        fields = [
            'pk',
            'invoice_no',
            'customer_name',
            'customer_type',
            'customer_address',
            'image'
        ]


class QuotationSerializer(serializers.HyperlinkedModelSerializer):
    quote_no = serializers.CharField()
    customer_name = serializers.SerializerMethodField()
    customer_type = serializers.SerializerMethodField()
    customer_address = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_customer_name(self, obj):
        return obj.customer.customer_name

    def get_customer_type(self, obj):
        return obj.customer.customer_type.customer_type_name

    def get_customer_address(self, obj):
        return f'{obj.customer.customer_address.address_1} {obj.customer.customer_address.address_2}'

    def get_image(self, obj):
        return obj.customer.image.url

    class Meta:
        model = Quotation
        fields = [
            'pk',
            'quote_no',
            'customer_name',
            'customer_type',
            'customer_address',
            'image'
        ]
