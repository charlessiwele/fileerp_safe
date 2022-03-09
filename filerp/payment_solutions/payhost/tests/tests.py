from django.test import TestCase
from payment_solutions.payhost.services.payhost_services import PayHostTokenPayment, PayHostCardPayment, \
    PayHostPayout, PayHostVault, PayHostFollowup


class FollowupRequestTest(TestCase):
    def setUp(self):
        self.followupRequest = PayHostFollowup()

    def test_settlement_transaction(self):
        settlement_transaction = self.followupRequest.settlement_transaction('28790224')
        assert settlement_transaction, 'response cannot be empty'

    def test_void_transaction(self):
        void_transaction = self.followupRequest.void_transaction('28790224')
        assert void_transaction, 'response cannot be empty'

    def test_refund_transaction(self):
        refund_transaction = self.followupRequest.refund_transaction('28790224', '100')
        assert refund_transaction, 'response cannot be empty'

    def test_query_transaction(self):
        query_transaction = self.followupRequest.query_transaction('6B739421-C177-903F-B23A-4BC1F09AB791')
        assert query_transaction, 'response cannot be empty'


class PayoutRequestTest(TestCase):
    def setUp(self):
        self.payoutRequest = PayHostPayout()

    def test_card_payout_request(self):
        card_payout_request = self.payoutRequest.card_payout_request(
            first_name='Joe',
            last_name='Soap',
            email='joes@example.com',
            card_number='4000000000000002',
            card_expiry_date='052015',
            merchant_order_id='order-1234',
            currency='ZAR',
            amount='100')
        assert card_payout_request, 'response cannot be empty'


class CardPaymentTest(TestCase):
    def setUp(self):
        self.card_payment_request = PayHostCardPayment()

    def test_card_payment_request(self):
        card_payment_request = self.card_payment_request.card_payment_request(
            first_name='Joe',
            last_name='Soap',
            email='joes@example.com',
            card_number='4000000000000002',
            card_expiry_date='052015',
            merchant_order_id='order-1234',
            currency='ZAR',
            amount='100',
            telephone='0861234567',
            mobile='0735552233',
            cvv='999',
            budget_period='0'
        )
        assert card_payment_request, 'response cannot be empty'

    def test_card_payment_tokenization_request(self):
        card_payment_tokenization_request = self.card_payment_request.card_payment_tokenization_request(
            first_name='Joe',
            last_name='Soap',
            email='joes@example.com',
            card_number='4000000000000002',
            card_expiry_date='052015',
            merchant_order_id='order-1234',
            currency='ZAR',
            amount='100',
            telephone='0861234567',
            mobile='0735552233',
            cvv='999',
            budget_period='0'
        )
        assert card_payment_tokenization_request, 'response cannot be empty'

    def test_card_payment_tokenized_request(self):
        card_payment_tokenized_request = self.card_payment_request.card_payment_tokenized_request(
            first_name='Joe',
            last_name='Soap',
            email='joes@example.com',
            merchant_order_id='order-1234',
            currency='ZAR',
            amount='100',
            telephone='0861234567',
            mobile='0735552233',
            cvv='123',
            budget_period='0',
            vault_id='eb9c11c5-e564-46e2-a087-2207ab8afadd'
        )
        assert card_payment_tokenized_request, 'response cannot be empty'

class TokenPaymentTest(TestCase):
    def setUp(self):
        self.token_payment_request = PayHostTokenPayment()

    def test_token_payment_request(self):
        token_payment_request = self.token_payment_request.token_payment_request(
            first_name='Joe',
            last_name='Soap',
            email='joes@example.com',
            merchant_order_id='order-1234',
            currency='ZAR',
            amount='100',
            token='2258098676320541501',
            token_detail='VCO'
        )
        assert token_payment_request, 'response cannot be empty'


class VaultTest(TestCase):
    def setUp(self):
        self.vaultRequest = PayHostVault()

    def test_card_delete_vault_request(self):
        card_delete_vault_request = self.vaultRequest.card_delete_vault_request('5c633bfa-5359-482e-b144-2949aa332c74')
        assert card_delete_vault_request, 'response cannot be empty'

    def test_card_lookup_vault_request(self):
        card_lookup_vault_request = self.vaultRequest.card_lookup_vault_request('c36a13e8-65a0-49fd-a12f-05fe78bf9eaa')
        assert card_lookup_vault_request, 'response cannot be empty'

    def test_card_vault_request(self):
        card_vault_request = self.vaultRequest.card_vault_request('5200000000000015', '112030')
        assert card_vault_request, 'response cannot be empty'
