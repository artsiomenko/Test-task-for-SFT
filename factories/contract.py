from operation.models import Contract
import factory


class ContractFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contract

    customer = 'Customer'
    price    = 0
