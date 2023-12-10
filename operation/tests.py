from factories.statement import StatementFactory
from factories.contract import ContractFactory
from factories.producer import ProducerFactory
from factories.product import ProductFactory
from .models import Contract

from rest_framework.test import APITestCase
from django.urls import reverse
import json


class OperationTests(APITestCase):
    def setUp(self):
        contract_1 = ContractFactory(customer='customer_1')
        contract_2 = ContractFactory(customer='customer_2')
        
        statement_1 = StatementFactory(contract=contract_1)
        statement_2 = StatementFactory(contract=contract_2)
        
        producer_1 = ProducerFactory(name='producer_1')
        producer_2 = ProducerFactory(name='producer_2')
        
        products_1 = [ProductFactory(producer=producer_1) for i in range(5)] + [ProductFactory(producer=producer_2) for i in range(3)]
        products_2 = [ProductFactory(producer=producer_1) for i in range(3)] + [ProductFactory(producer=producer_2) for i in range(5)]
        
        statement_1.products.set(products_1)
        statement_2.products.set(products_2)

    def test_get_producer_id(self):
        contract_id =  Contract.objects.get(customer='customer_2').id
        url = f'/get_producer_id/{contract_id}'
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'producer_ids': [1, 2]})
