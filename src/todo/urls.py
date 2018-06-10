from django.conf.urls import url
from django.conf.urls import include
from todo import views
from rest_framework.routers import DefaultRouter


#Create a router and register our viewset with it
router=DefaultRouter(trailing_slash=False)
router.register(r'todos', views.TodoItemViewSet)

#API  URLS are now automatically detected by the router
urlpatterns=[
	url(r'^',include(router.urls)),
]