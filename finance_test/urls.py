from django.urls import path, include
from django.contrib import admin

from operation.views import get_producer_id
from operation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('operation.urls')),
]
