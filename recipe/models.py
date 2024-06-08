from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
	"""Recipe Object"""

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=300)
	time_minutes = models.PositiveSmallIntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)