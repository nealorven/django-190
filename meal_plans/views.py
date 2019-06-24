from django.shortcuts import render


def index(request):
	""" Домашняя страница приложения Learning Log """
	return render(request, 'meal_plans/index.html')
