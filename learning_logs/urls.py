""" Определяет схемы URL для learning_logs """

from django.conf.urls import url

from . import views

# Переменная urlpatterns в этом модуле представляет собой список страниц, 
# которые могут запрашиваться из приложения learning_logs.
urlpatterns = [
	# Домашняя страница. Сравнивает url в urlpatterns которые относятся
	# к learning_logs приложению.
	url(r'^$', views.index, name='index'),
	url(r'^topics/', views.topics, name='topics'),
]
