# urls.py (en la carpeta mi_app)

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('main/', TemplateView.as_view(template_name='main.html'), name='main'),
]
