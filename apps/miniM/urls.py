from django.conf.urls import url
from apps.miniM.views import testP_view

urlpatterns = [
    url(r'miniM/', testP_view, name="home"),
]