from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.apiviews import CategoriaDetalle, CategoriaList, LoginView, \
    ProductoList, ProductoDetalle, ProductoViewSet, SubCategoriaAdd, \
        SubCategoriaList, UserCreate

router = DefaultRouter()
router.register('v2/productos/', ProductoViewSet, basename='productos')

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle'),
    path('v1/categorias/', CategoriaList.as_view(), name='categoria_save'),
    #path('v1/subcategorias/', SubCategoriaList.as_view(), name='subcategoria_save'),
    path('v1/categorias/<int:pk>', CategoriaDetalle.as_view(), name='categoria_detalle'),
    path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(), name='subcategoria_list'),
    path('v1/categorias/<int:cat_pk>/addsubcategorias/', SubCategoriaAdd.as_view(), name='subcategoria_add'),
    
    path('v3/usuarios/', UserCreate.as_view(), name='usuario_crear'),
    
    path('v4/login/', LoginView.as_view(), name='login'),
    path('v4/login-drf/', views.obtain_auth_token, name='login-drf'),
]

urlpatterns += router.urls