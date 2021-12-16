from django.urls import path, include, re_path
from toys import views

urlpatterns = [
	# path(r'^toys/$', views.toy_list),
	# path(r'^toys/(?P<pk>[0-9]+)$', views.toy_detail),
 	re_path(r'^toys/$', views.toy_list),
    re_path(r'^toys/(?P<pk>[0-9]+)$', views.toy_detail),




]
