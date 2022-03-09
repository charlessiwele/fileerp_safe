import os

from report_center.pdf_handler.services.pdf_handler import PdfHandler
from report_center.report_templates.pdf_templates.invoice import InvoiceTemplate
from report_center.report_templates.pdf_templates.quotation import QuotationTemplate


def generate_invoice(data):
    """ This function performs necessary logic for generating an invoice """
    invoice = InvoiceTemplate(data)

    total = PdfHandler.get_total(data)

    pages = PdfHandler.calculate_number_of_pages(data)

    invoice.write_invoice_content(total, pages)

    invoice.write_notes()

    # In case the directory doesnt exist
    os.makedirs('public/pdf/invoices/', exist_ok=True)

    file_location = f'public/pdf/invoices/{data["invoice_number"]}.pdf'

    invoice.pdf.output(file_location)
    return file_location


def generate_quotation(data):
    """ This function performs necessary logic for generating an invoice """
    quotation = QuotationTemplate(data)

    total = PdfHandler.get_total(data)

    pages = PdfHandler.calculate_number_of_pages(data)

    quotation.write_quotation_content(total, pages)

    quotation.write_notes()

    # In case the directory doesnt exist
    os.makedirs('public/pdf/quotations/', exist_ok=True)

    file_location = f'public/pdf/quotations/{data["quotation_number"]}.pdf'

    quotation.pdf.output(file_location)
    return file_location

