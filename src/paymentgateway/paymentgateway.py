from common.logger import Logger
from .premiumpaymentgateway import PremiumPaymentGateway
from .expensivepaymentgateway import ExpensivePaymentGateway
from .cheappaymentgateway import CheapPaymentGateway
from .payment import Payment

import os

class PaymentGateway(Payment):

    def __init__(self):
        self.premiumgateway = PremiumPaymentGateway()
        self.expensivegateway = ExpensivePaymentGateway()
        self.cheapgateway = CheapPaymentGateway()

    def select_payment_provider(self, input_data):
        amount = float(input_data['Amount'])
        if 0 < amount < 20:
            return self.cheapgateway.process_payment(amount)
        elif 20 <= amount < 500:
            return self.expensivegateway.process_payment(amount)
        else:
            return self.premiumgateway.process_payment(amount)
        