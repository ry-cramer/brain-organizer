from django.urls import path
from .views import index

urlpatterns = [
    path('<path:route>', index),
]