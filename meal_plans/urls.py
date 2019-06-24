""" Определяет схемы URL для meal_plans """

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index')
]
