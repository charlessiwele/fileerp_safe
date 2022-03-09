from payment_solutions.payhost.settings.payhost_settings import PAYGATE_ID, PAYGATE_PASSWORD

class SingleVaultRequestModel:
    @staticmethod
    def get_model(card_number, card_expiry_date):
        single_follow_up_request = {
            'Account': {
                'PayGateId': PAYGATE_ID,
                'Password': PAYGATE_PASSWORD
            },
            'CardNumber': card_number,
            'CardExpiryDate': card_expiry_date
        }
        return single_follow_up_request


class SingleFollowUpQueryRequestModel:
    @staticmethod
    def get_model(pay_request_id):
        single_follow_up_request = {
            'Account': {
                'PayGateId': PAYGATE_ID,
                'Password': PAYGATE_PASSWORD
            },
            'PayRequestId': pay_request_id
        }
        return single_follow_up_request


class SingleFollowUpVoidRequestModel:
    @staticmethod
    def get_model(transaction_id, transaction_type):
        single_follow_up_request = {
            'Account': {
                'PayGateId': PAYGATE_ID,
                'Password': PAYGATE_PASSWORD
            },
            'TransactionId': transaction_id,
            'TransactionType': transaction_type
        }
        return single_follow_up_request


class SingleFollowUpSettlementRequestModel:
    @staticmethod
    def get_model(transaction_id):
        single_follow_up_request = {
            'Account': {
                'PayGateId': PAYGATE_ID,
                'Password': PAYGATE_PASSWORD
            },
            'TransactionId': transaction_id,
        }
        return single_follow_up_request


class SingleFollowUpRefundRequestModel:
    @staticmethod
    def get_model(transaction_id, amount):
        single_follow_up_request = {
            'Account': {
                'PayGateId': PAYGATE_ID,
                'Password': PAYGATE_PASSWORD
            },
            'TransactionId': transaction_id,
            'Amount': amount,
        }
        return single_follow_up_request


class SingleLookUpVaultRequestModel:
    def get_model(self, vault_id):
        single_follow_up_request = {
            'Account': {
                'PayGateId': PAYGATE_ID,
                'Password': PAYGATE_PASSWORD
            },
            'VaultId': vault_id,
        }
        return single_follow_up_request


class SingleDeleteVaultRequestModel(SingleLookUpVaultRequestModel):
    pass


class SinglePayoutRequestModel:
    @staticmethod
    def get_model(first_name, last_name, email, card_number, card_expiry_date, merchant_order_id, currency, amount):
        single_follow_up_request = {
            'Account': {
                'PayGateId': PAYGATE_ID,
                'Password': PAYGATE_PASSWORD
            },
            'Customer': {
                'FirstName': first_name,
                'LastName': last_name,
                'Email': email,
            },
            'CardNumber': card_number,
            'CardExpiryDate': card_expiry_date,
            'Order': {
                'MerchantOrderId': merchant_order_id,
                'Currency': currency,
                'Amount': amount
            },

        }
        return single_follow_up_request


class CardPaymentRequestModel:
        @staticmethod
        def get_card_model(first_name, last_name, telephone, mobile, email, card_number, card_expiry_date, cvv,
                      budget_period, merchant_order_id, currency, amount):
            single_follow_up_request = {
                'Account': {
                    'PayGateId': PAYGATE_ID,
                    'Password': PAYGATE_PASSWORD
                },
                'Customer': {
                    'FirstName': first_name,
                    'LastName': last_name,
                    'Telephone': telephone,
                    'Mobile': mobile,
                    'Email': email,
                },
                'CardNumber': card_number,
                'CardExpiryDate': card_expiry_date,
                'CVV': cvv,
                'BudgetPeriod': budget_period,
                'Order': {
                    'MerchantOrderId': merchant_order_id,
                    'Currency': currency,
                    'Amount': amount
                },

            }
            return single_follow_up_request

        @staticmethod
        def get_card_tokenization_model(first_name, last_name, telephone, mobile, email, card_number, card_expiry_date, cvv,
                      budget_period, merchant_order_id, currency, amount):
            single_follow_up_request = {
                'Account': {
                    'PayGateId': PAYGATE_ID,
                    'Password': PAYGATE_PASSWORD
                },
                'Customer': {
                    'FirstName': first_name,
                    'LastName': last_name,
                    'Telephone': telephone,
                    'Mobile': mobile,
                    'Email': email,
                },
                'CardNumber': card_number,
                'CardExpiryDate': card_expiry_date,
                'CVV': cvv,
                'Vault': True,
                'BudgetPeriod': budget_period,
                'Order': {
                    'MerchantOrderId': merchant_order_id,
                    'Currency': currency,
                    'Amount': amount
                },

            }
            return single_follow_up_request

        @staticmethod
        def get_tokenized_card_model(first_name, last_name, telephone, mobile, email, vault_id, cvv,
                      budget_period, merchant_order_id, currency, amount):
            single_follow_up_request = {
                'Account': {
                    'PayGateId': PAYGATE_ID,
                    'Password': PAYGATE_PASSWORD
                },
                'Customer': {
                    'FirstName': first_name,
                    'LastName': last_name,
                    'Telephone': telephone,
                    'Mobile': mobile,
                    'Email': email,
                },
                'VaultId': vault_id,
                'CVV': cvv,
                'BudgetPeriod': budget_period,
                'Order': {
                    'MerchantOrderId': merchant_order_id,
                    'Currency': currency,
                    'Amount': amount
                },

            }
            return single_follow_up_request


class TokenPaymentRequestModel:
    @staticmethod
    def get_model(first_name, last_name, email, token, token_detail, merchant_order_id, currency, amount):
        single_follow_up_request = {
            'Account': {
                'PayGateId': PAYGATE_ID,
                'Password': PAYGATE_PASSWORD
            },
            'Customer': {
                'FirstName': first_name,
                'LastName': last_name,
                'Email': email,
            },
            'Token': token,
            'TokenDetail': token_detail,
            'Order': {
                'MerchantOrderId': merchant_order_id,
                'Currency': currency,
                'Amount': amount
            },

        }
        return single_follow_up_request

