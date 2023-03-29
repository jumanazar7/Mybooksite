from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotFound



def index_page(request):
    return render(request, 'main/index.html')


def get_product(request, product_id, product_name="Noma'lum"):
    text = f"<b>Product ID: {product_id}<br>Product Name: {product_name}</b>"
    return HttpResponse(text)

def redirection(request):
    return HttpResponseRedirect("/main/notfound/")

def bad_request_400(request):
    return HttpResponseBadRequest("<h1>Bad Request</h1>")

def not_found(request):
    return HttpResponseNotFound("<h1>Page Not Found</h1>")

def users(request):
    user_id = request.GET.get('id', 0)
    user_name = request.GET.get('username', 'Noma\'lum')
    text = f"<b>USER ID: {user_id}<br>User Name: {user_name}</b>"
    return HttpResponse(text)
