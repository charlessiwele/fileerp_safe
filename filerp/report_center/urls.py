from django.urls import path
from report_center.views import GeneratePDFInvoiceView, GeneratePDFQuotationView, GenerateAndEmailPDFInvoiceView, \
    GenerateAndEmailPDFQuotationView

urlpatterns = [
    path('pdf/generate_invoice/<pk>', GeneratePDFInvoiceView.as_view(), name='generate_pdf_invoice'),
    path('pdf/generate_quotation/<pk>', GeneratePDFQuotationView.as_view(), name='generate_pdf_quotation'),
    path('pdf/generate_invoice_and_email/<pk>', GenerateAndEmailPDFInvoiceView.as_view(), name='generate_and_email_pdf_invoice'),
    path('pdf/generate_quotation_and_email/<pk>', GenerateAndEmailPDFQuotationView.as_view(), name='generate_and_email_pdf_quotation'),
]