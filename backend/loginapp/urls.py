from django.urls import path
from .views import login_view

urlpatterns = [
    path('login/', login_view), # No debe haber ningún include aquí que apunte hacia atrás o a sí mismo
]