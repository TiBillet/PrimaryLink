from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('<pin_link>', views.send_url_based_on_pin, name='pin_link'),
]