from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	url(r'^search$',views.search,name='search'),
	url(r'^res$',views.res,name='res'),
    url(r'^restuarant$',views.restuarant,name='restuarant'),
    url(r'^$',views.login,name='login'),
    url(r'^login$',views.login,name='login'),
    url(r'^rev2$',views.rev2,name='rev2'),
    url(r'^logout$',views.logout,name='logout'),




    url(r'^signup$',views.signup,name='signup'),

    # url(r'^demo$',views.demo,name='demo'),
    # url(r'^demo2$',views.demo2,name='demo2'),
    # url(r'^demo3$',views.demo3,name='demo3'),




	
]