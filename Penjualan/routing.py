from django.urls import re_path
from .consumers import ProdukKeluarConsumer

websocket_urlpatterns = [
    re_path(r"ws/produk_keluar/$", ProdukKeluarConsumer.as_asgi()),
]