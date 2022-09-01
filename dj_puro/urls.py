from django.urls import URLPattern, path
from .views import listCategoria, detailCategoria

urlpatterns = [
    path('categorias/', listCategoria, name='list_categoria'),
    path('categorias/<int:pk>', detailCategoria, name='detail_categoria'),
]
