from django.conf.urls import url, include
from . import views




urlpatterns = [
    #url(r'^regist/$', views.registUser, name=regist),
    #url(r'^login/$', views.login, name=login),
    #url(r'^logout/$', views.logout, name=logout),
    #url(r'^newbundle/$', views.newProductBundle, name=newbundle),
    #url(r'^editbundle/$', views.editProductBundle, name=editbundle),
    #access callbackData from SIGFOX
    url(r'^receiveCallback$', views.receiveCallback, name='receiveCallback'),
]

