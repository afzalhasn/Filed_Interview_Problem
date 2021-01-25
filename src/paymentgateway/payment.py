import abc

class Payment:

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def select_payment_provider(self, input_data):
        pass
