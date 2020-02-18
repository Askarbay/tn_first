from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from zakaz.models import Zakaz, Zakazdoc


def basket_adding(request):
    return_dict = dict()
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    user_id = data.get("user_id")
    new_product = Zakaz.objects.get_or_create(lot_id=product_id, klyent_id=user_id,)
    return JsonResponse(return_dict)


def basket_adding_doc(request):
    return_dict = dict()
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    user_id = data.get("user_id")
    new_product = Zakazdoc.objects.get_or_create(lots_id=product_id, klyenty_id=user_id,)
    return JsonResponse(return_dict)
