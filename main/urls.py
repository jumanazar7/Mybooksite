from django.urls import path, re_path
from .views import get_product, users, redirection, bad_request_400, not_found, index_page


urlpatterns = [
    path('', index_page, name="index"),
    path('product/<int:product_id>/', get_product, name="get_product_without_name"),
    re_path(r'^product/(?P<product_id>\d+)/(?P<product_name>\D+)/$', get_product, name="get_product"),
    path('users/', users, name="users"),
    path('cart/', redirection, name="cart_redirect"),
    path('bad/', bad_request_400, name="check_bad_request"),
    path('notfound/', not_found, name="page_not_found")
]

# GET, POST
