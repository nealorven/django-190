from django.db import models


class Day(models.Model):
	""" Указываем день недели """
	text = models.CharField(max_length=10)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		""" Возвращает строковое представление модели """
		return self.text


class Meal(models.Model):
	""" План потребления еды на один день """
	day = models.ForeignKey(Day, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		""" Дополнительная информация по управлению моделью Day """
		verbose_name_plural = 'meals'

	def __str__(self):
		""" Возвращает строковое представление модели """
		return f"{self.text[:50]}..." if len(self.text) > 50 else self.text
