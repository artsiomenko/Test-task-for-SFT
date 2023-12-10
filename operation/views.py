from django.http import JsonResponse
from .models import Statement
from django.core.serializers import serialize
from rest_framework.response import Response


def get_producer_id(request, contract_id):
    producers = Statement.objects.get(contract=contract_id).products.values('producer').distinct()
    return JsonResponse ({'producer_ids' : [id['producer'] for id in producers]})
