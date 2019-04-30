from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^changeDB',views.changeDB),
    url(r'^getDB',views.getDB),

    url(r'^queryId',views.queryId),
    url(r'^ranksAverage', views.ranksAverage),
    url(r'^ranksSingle', views.ranksSingle),
    # url...
]