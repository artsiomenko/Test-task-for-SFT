from factories.producer import ProducerFactory
from operation.models import Product
import factory


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = 'car'
    producer = factory.SubFactory(ProducerFactory)
