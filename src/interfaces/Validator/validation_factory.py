import abc

class GatewayValidation:

    def __init__(self):
        pass

    @abc.abstractmethod
    def post_method_validation(self, request):
        pass
