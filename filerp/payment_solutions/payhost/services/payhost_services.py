# Payhost Namespaces
from payment_solutions.payhost.models.payhost_models import SingleDeleteVaultRequestModel, \
    SingleLookUpVaultRequestModel, \
    SingleVaultRequestModel, SingleFollowUpQueryRequestModel, SingleFollowUpVoidRequestModel, \
    SingleFollowUpSettlementRequestModel, SingleFollowUpRefundRequestModel, SinglePayoutRequestModel, \
    CardPaymentRequestModel, TokenPaymentRequestModel
from requests import Session, Response
from requests.auth import HTTPBasicAuth
from zeep import Client, Settings, helpers, Transport

from payment_solutions.payhost.settings.payhost_settings import PAYGATE_ID, PAYGATE_PASSWORD, TRANSACTION_ID
from payment_solutions.payhost.types.payhost_transaction_types import TransactionType


class PayHostSession:
    """
        Vault requests allow merchants to manage what is stored by the PayVault tokenisation service.
        Please note that currently PayVault only supports the tokenisation of credit card data.
        """

    def __init__(self) -> None:
        super().__init__()
        self.url_wsdl = "https://secure.paygate.co.za/payhost/process.trans?wsdl"
        settings = Settings(strict=False, xml_huge_tree=True)

        session = Session()
        session.auth = HTTPBasicAuth(PAYGATE_ID, PAYGATE_PASSWORD)
        wsdl_client = Client(self.url_wsdl, transport=Transport(session=session), settings=settings)
        self.wsdl_services = wsdl_client.service


class PayHostFollowup(PayHostSession):
    """
    Follow up requests allow a Merchant multiple options after processing has taken place.
    These can be either Settling a transaction (if a merchant is not setup for AutoSettle), refunding a transaction,
    querying a transaction status, etc.
    """


    def query_transaction(self, pay_request_id) -> Response:
        """
        The Query function allows you to query the final status of previously processed transactions.
        The Query function will accept a PayRequestId, TransId or a Reference as a search key.
        :return:
        """
        try:
            single_follow_up_request = SingleFollowUpQueryRequestModel()
            request_response = self.wsdl_services.SingleFollowUp(QueryRequest=single_follow_up_request.get_model(pay_request_id))
            print(request_response)
            return request_response
        except Exception as e:
            print(e)

    def void_transaction(self, transaction_id) -> Response:
        """
        The void function allows merchants to void transactions that are not yet settled or refunded. Settlements and
        Refunds can only be stopped using the Void request if they have not yet been submitted to the acquiring bank.
        :return:
        """
        try:
            single_follow_up_request = SingleFollowUpVoidRequestModel()
            request_response = self.wsdl_services.SingleFollowUp(VoidRequest=single_follow_up_request.get_model(transaction_id, TransactionType.SETTLEMENT))
            print(request_response)
            return request_response
        except Exception as e:
            print(e)

    def settlement_transaction(self, transaction_id) -> Response:
        """
        This function allows the merchant to settle an authorisation where AutoSettle is turned off
        :return:
        """
        try:
            single_follow_up_request = SingleFollowUpSettlementRequestModel()
            request_response = self.wsdl_services.SingleFollowUp(SettlementRequest=single_follow_up_request.get_model(transaction_id))
            print(request_response)
            return request_response
        except Exception as e:
            print(e)

    def refund_transaction(self, transaction_id, amount) -> Response:
        """
        This function allows the merchant to refund a transaction that has already been settled
        :return:
        """
        try:
            single_follow_up_request = SingleFollowUpRefundRequestModel()
            request_response = self.wsdl_services.SingleFollowUp(RefundRequest=single_follow_up_request.get_model(transaction_id, amount))
            print(request_response)
            return request_response
        except Exception as e:
            print(e)


class PayHostVault(PayHostSession):
    """
    Vault requests allow merchants to manage what is stored by the PayVault tokenisation service.
    Please note that currently PayVault only supports the tokenisation of credit card data.
    """

    def card_vault_request(self, card_number, card_expiry_date) -> Response:
        single_follow_up_request = SingleVaultRequestModel()
        request_response = self.wsdl_services.SingleVault(CardVaultRequest=single_follow_up_request.get_model(card_number, card_expiry_date))
        print(request_response)
        return request_response

    def card_lookup_vault_request(self, vault_id) -> Response:
        single_follow_up_request = SingleLookUpVaultRequestModel()
        request_response = self.wsdl_services.SingleVault(LookUpVaultRequest=single_follow_up_request.get_model(vault_id))
        print(request_response)
        return request_response

    def card_delete_vault_request(self, vault_id) -> Response:
        single_follow_up_request = SingleDeleteVaultRequestModel()
        request_response = self.wsdl_services.SingleVault(DeleteVaultRequest=single_follow_up_request.get_model(vault_id))
        print(request_response)
        return request_response


class PayHostPayout(PayHostSession):

    def card_payout_request(self, first_name, last_name, email, card_number, card_expiry_date, merchant_order_id, currency, amount) -> Response:
        """
        Payout requests allow a Merchant to process pay-outs to their customers. Please note that pay-outs can only be done
        if the functionality is supported by the relevant acquirer or payment method.
        """
        single_follow_up_request = SinglePayoutRequestModel()
        request_response = self.wsdl_services.SinglePayout(CardPayoutRequest=single_follow_up_request.get_model(
            first_name, last_name, email, card_number, card_expiry_date, merchant_order_id, currency, amount)
        )
        print(request_response)
        return request_response


class PayHostCardPayment(PayHostSession):
    def card_payment_request(self, first_name, last_name, telephone, mobile, email, card_number, card_expiry_date, cvv,
                             budget_period, merchant_order_id, currency, amount) -> Response:
        """
        The merchant sends the relevant encrypted data to PayGate along with other transaction data.
        PayGate decrypts the data received and processes the authorisation to the acquiring bank.
        Once the acquiring bank has responded with the authorisation status PayGate sends this response to the merchant.
        """
        single_follow_up_request = CardPaymentRequestModel()
        request_response = self.wsdl_services.SinglePayment(CardPaymentRequest=single_follow_up_request.get_card_model(
            first_name, last_name, telephone, mobile, email, card_number, card_expiry_date, cvv,
            budget_period, merchant_order_id, currency, amount)
        )
        print(request_response)
        return request_response

    def card_payment_tokenization_request(self, first_name, last_name, telephone, mobile, email, card_number,
                                          card_expiry_date, cvv, budget_period, merchant_order_id, currency, amount) -> Response:
        """
        This field is used to indicate whether a PayVault token should be issued for the credit card used to make the
        payment. If True the credit card number will be added to PayVault and the associated Token will be returned
        in the response to the merchant.
        :param first_name:
        :param last_name:
        :param telephone:
        :param mobile:
        :param email:
        :param card_number:
        :param card_expiry_date:
        :param cvv:
        :param budget_period:
        :param merchant_order_id:
        :param currency:
        :param amount:
        :return:
        """
        single_follow_up_request = CardPaymentRequestModel()
        request_response = self.wsdl_services.SinglePayment(
            CardPaymentRequest=single_follow_up_request.get_card_tokenization_model(
                first_name=first_name, last_name=last_name, telephone=telephone, mobile=mobile, email=email,
                card_number=card_number, card_expiry_date=card_expiry_date, cvv=cvv, budget_period=budget_period,
                merchant_order_id=merchant_order_id, currency=currency, amount=amount
            )
        )
        print(request_response)
        return request_response

    def card_payment_tokenized_request(self, first_name, last_name, telephone, mobile, email, cvv,
                             budget_period, merchant_order_id, currency, amount, vault_id) -> Response:
        """
         If a PayVault token GUID is sent the credit card transaction will be processed using the credit card associated
         with the token. A credit card CVV value will still be required. 3D Secure authentication may also be required.
        :param first_name:
        :param last_name:
        :param telephone:
        :param mobile:
        :param email:
        :param cvv:
        :param budget_period:
        :param merchant_order_id:
        :param currency:
        :param amount:
        :param vault_id:
        :return:
        """
        single_follow_up_request = CardPaymentRequestModel()
        request_response = self.wsdl_services.SinglePayment(CardPaymentRequest=single_follow_up_request.get_tokenized_card_model(
            first_name=first_name, last_name=last_name, telephone=telephone, mobile=mobile, email=email, vault_id=vault_id,
            cvv=cvv, budget_period=budget_period, merchant_order_id=merchant_order_id, currency=currency, amount=amount)
        )
        print(request_response)
        return request_response


class PayHostTokenPayment(PayHostSession):
    def token_payment_request(self, first_name, last_name, email, token, token_detail, merchant_order_id, currency, amount) -> Response:
        """
        The merchant sends the relevant encrypted data to PayGate along with other transaction data.
        PayGate decrypts the data received and processes the authorisation to the acquiring bank.
        Once the acquiring bank has responded with the authorisation status PayGate sends this response to the merchant.
        """
        single_follow_up_request = TokenPaymentRequestModel()
        request_response = self.wsdl_services.SinglePayment(TokenPaymentRequest=single_follow_up_request.get_model(
            first_name=first_name, last_name=last_name, merchant_order_id=merchant_order_id, currency=currency,
            amount=amount, email=email, token=token, token_detail=token_detail)
        )
        print(request_response)
        return request_response
