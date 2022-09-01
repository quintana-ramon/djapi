from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from dj_puro.models import Categoria

# Create your views here.


def listCategoria(request):
    MAX_OBJECTS = 20
    cat = Categoria.objects.all()[:MAX_OBJECTS]
    data = {"results": list(cat.values("descripcion", "activo"))}
    return JsonResponse(data)


def detailCategoria(request, pk):
    cat = get_object_or_404(Categoria, pk=pk)
    data = {"result": {"descripcion": cat.descripcion, "activo": cat.activo}}

    return JsonResponse(data)
