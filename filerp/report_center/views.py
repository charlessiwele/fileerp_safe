import datetime
from django.http import HttpResponse
from rest_framework.views import APIView
from data_center.models import CurrentBank, Invoice, Quotation
from report_center.email_handlers.services.send_email_with_pdf_attachments import EmailManager
from report_center.pdf_handler.services.pdf_handler import PdfHandler
from report_center.services.services import generate_invoice, generate_quotation


class GeneratePDFInvoiceView(APIView):

    @staticmethod
    def get(*args, **kwargs):
        product_data = []
        data = {}
        invoice = Invoice.objects.get(pk=kwargs.get('pk'))

        invoiceproduct_set = list(invoice.invoiceproduct_set.all())
        for invoiceproduct in invoiceproduct_set:
            product_price = invoiceproduct.product.product_price
            if invoiceproduct.check_out and invoiceproduct.check_in:
                date_delta = invoiceproduct.check_out - invoiceproduct.check_in
                days = date_delta.days
                if days > 0:
                    product_price = float(product_price) * int(days)

            product_data.append({
                'title': PdfHandler.generate_invoice_product_display_name(invoiceproduct),
                'quantity': invoiceproduct.product_quantity,
                'price': product_price,
                'sku': invoiceproduct.product.id,
                'total': invoiceproduct.calculate_line_total()
            })

        data['products'] = product_data
        data["date"] = datetime.datetime.now().strftime('%d/%m/%Y')
        data["invoice_number"] = invoice.invoice_no
        data["client_name"] = invoice.customer.customer_name
        data["client_email"] = invoice.customer.customer_address.email
        if args[0].user.first_name:
            data["user"] = f'{args[0].user.first_name} {args[0].user.last_name}'
        else:
            data["user"] = f'{args[0].user.username}'

        bank_details = f'Bank Details\n' \
                f'Bank Name: {CurrentBank.bank_name}\n ' \
                f'Account Type: {CurrentBank.account_type}\n ' \
                f'Account Holder: {CurrentBank.account_holder}\n ' \
                f'Account No.: {CurrentBank.account_no}'

        data['notes'] = [bank_details]
        data['invoiceproduct_set'] = invoiceproduct_set

        pm = generate_invoice(data)
        pdf_file = open(pm, 'rb')
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={pm}'
        return response


class GenerateAndEmailPDFInvoiceView(APIView):

    @staticmethod
    def get(*args, **kwargs):
        product_data = []
        data = {}
        invoice = Invoice.objects.get(pk=kwargs.get('pk'))

        invoiceproduct_set = list(invoice.invoiceproduct_set.all())
        for invoiceproduct in invoiceproduct_set:
            product_price = invoiceproduct.product.product_price
            if invoiceproduct.check_out and invoiceproduct.check_in:
                date_delta = invoiceproduct.check_out - invoiceproduct.check_in
                days = date_delta.days
                if days > 0:
                    product_price = float(product_price) * int(days)

            product_data.append({
                'title': PdfHandler.generate_invoice_product_display_name(invoiceproduct),
                'quantity': invoiceproduct.product_quantity,
                'price': product_price,
                'sku': invoiceproduct.product.id,
                'total': invoiceproduct.calculate_line_total()
            })

        data['products'] = product_data
        data["date"] = datetime.datetime.now().strftime('%d/%m/%Y')
        data["invoice_number"] = invoice.invoice_no
        data["client_name"] = invoice.customer.customer_name
        data["client_email"] = invoice.customer.customer_address.email
        if args[0].user.first_name:
            data["user"] = f'{args[0].user.first_name} {args[0].user.last_name}'
            signing_email_user = data["user"]
        else:
            data["user"] = f'{args[0].user.username}'
            signing_email_user = f'C Siwele'

        bank_details = f'Bank Details\n' \
                f'Bank Name: {CurrentBank.bank_name}\n ' \
                f'Account Type: {CurrentBank.account_type}\n ' \
                f'Account Holder: {CurrentBank.account_holder}\n ' \
                f'Account No.: {CurrentBank.account_no}'

        data['notes'] = [bank_details]
        data['invoiceproduct_set'] = invoiceproduct_set

        pm = generate_invoice(data)
        pdf_file = open(pm, 'rb')
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={pm}'
        email_response_result = EmailManager().send_email_with_pdf_attachments(
                sender_email='test@theangelsguesthouse.co.za',
                sender_password='Carhorsebucket1!',
                email_recipients=(data["client_email"],),
                email_subject=f'Invoice {data["client_name"] }',
                attachment_file_path=pm,
                email_body=f'Good day, \nPlease find attached invoice for your convenience.\nKind Regards \n{signing_email_user}')
        print(email_response_result)
        return response


class GeneratePDFQuotationView(APIView):

    @staticmethod
    def get(*args, **kwargs):
        product_data = []
        data = {}
        quotation = Quotation.objects.get(pk=kwargs.get('pk'))

        quotationproduct_set = list(quotation.quotationproduct_set.all())
        for quotationproduct in quotationproduct_set:
            product_price = quotationproduct.product.product_price
            if quotationproduct.check_out and quotationproduct.check_in:
                date_delta = quotationproduct.check_out - quotationproduct.check_in
                days = date_delta.days
                if days > 0:
                    product_price = float(product_price) * int(days)


            product_data.append({
                'title': PdfHandler.generate_invoice_product_display_name(quotationproduct),
                'quantity': quotationproduct.product_quantity,
                'price': product_price,
                'sku': quotationproduct.product.id,
                'total': quotationproduct.calculate_line_total()
            })

        data['products'] = product_data
        data["date"] = datetime.datetime.now().strftime('%d/%m/%Y')
        data["quotation_number"] = quotation.quote_no
        data["client_name"] = quotation.customer.customer_name
        data["client_email"] = quotation.customer.customer_address.email
        if args[0].user.first_name:
            data["user"] = f'{args[0].user.first_name} {args[0].user.last_name}'
        else:
            data["user"] = f'{args[0].user.username}'

        bank_details = f'Bank Details\n' \
                f'Bank Name: {CurrentBank.bank_name}\n ' \
                f'Account Type: {CurrentBank.account_type}\n ' \
                f'Account Holder: {CurrentBank.account_holder}\n ' \
                f'Account No.: {CurrentBank.account_no}'

        data['notes'] = [bank_details]
        data['quotationproduct_set'] = quotationproduct_set

        pm = generate_quotation(data)
        pdf_file = open(pm, 'rb')
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={pm}'
        return response


class GenerateAndEmailPDFQuotationView(APIView):

    @staticmethod
    def get(*args, **kwargs):
        product_data = []
        data = {}
        quotation = Quotation.objects.get(pk=kwargs.get('pk'))

        quotationproduct_set = list(quotation.quotationproduct_set.all())
        for quotationproduct in quotationproduct_set:
            product_price = quotationproduct.product.product_price
            if quotationproduct.check_out and quotationproduct.check_in:
                date_delta = quotationproduct.check_out - quotationproduct.check_in
                days = date_delta.days
                if days > 0:
                    product_price = float(product_price) * int(days)


            product_data.append({
                'title': PdfHandler.generate_invoice_product_display_name(quotationproduct),
                'quantity': quotationproduct.product_quantity,
                'price': product_price,
                'sku': quotationproduct.product.id,
                'total': quotationproduct.calculate_line_total()
            })

        data['products'] = product_data
        data["date"] = datetime.datetime.now().strftime('%d/%m/%Y')
        data["quotation_number"] = quotation.quote_no
        data["client_name"] = quotation.customer.customer_name
        data["client_email"] = quotation.customer.customer_address.email
        if args[0].user.first_name:
            data["user"] = f'{args[0].user.first_name} {args[0].user.last_name}'
            signing_email_user = data["user"]
        else:
            data["user"] = f'{args[0].user.username}'
            signing_email_user = f'C Siwele'

        bank_details = f'Bank Details\n' \
                f'Bank Name: {CurrentBank.bank_name}\n ' \
                f'Account Type: {CurrentBank.account_type}\n ' \
                f'Account Holder: {CurrentBank.account_holder}\n ' \
                f'Account No.: {CurrentBank.account_no}'

        data['notes'] = [bank_details]
        data['quotationproduct_set'] = quotationproduct_set

        pm = generate_quotation(data)
        pdf_file = open(pm, 'rb')
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={pm}'
        EmailManager().send_email_with_pdf_attachments(
                sender_email='test@theangelsguesthouse.co.za',
                sender_password='Carhorsebucket1!',
                email_recipients=(data["client_email"],),
                email_subject=f'Quotation {data["client_name"] }',
                attachment_file_path=pm,
                email_body=f'Good day, \nPlease find attached quote for your convenience.\nKind Regards \n{signing_email_user}')
        return response

