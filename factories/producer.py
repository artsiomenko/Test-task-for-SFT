from operation.models import Producer
import factory


class ProducerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Producer

    name = factory.Faker('name')
