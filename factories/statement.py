from factories.contract import ContractFactory
from operation.models import Statement
import factory


class StatementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Statement

    contract  = factory.SubFactory(ContractFactory)
