from .views import get_producer_id
from django.urls import path
from . import views

app_name = 'operation'

urlpatterns = [
    path('get_producer_id/<int:contract_id>', views.get_producer_id, name='producer_id'),
]
