from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from manage import main
from . import views
app_name = "map"
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('service', views.service, name='service'),
    # re_path(r'^(?P<pk>[0-9]+)/$', views.showMap, name='show'),
]
