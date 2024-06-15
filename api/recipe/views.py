from rest_framework import viewsets

from recipe.models import Recipe
from recipe.serializers import RecipeSerializer

class RecipeViewset(viewsets.ModelViewSet):
	queryset = Recipe.objects.all()
	serializer_class = RecipeSerializer