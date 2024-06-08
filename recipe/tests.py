from tests.api_request_factory import APIViewRequestFactory
from rest_framework import status
from recipe.views import RecipeViewset
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer


class TestRecipeViewset(APIViewRequestFactory):
	view_name = RecipeViewset

	def setUp(self):
		Recipe.objects.create(user=self.authenticated_user, title="Breakfast", time_minutes=10, price=10.0)

	def tearDown(self):
		Recipe.objects.all().delete()

	def test_list_of_recipes(self):
		response = self.send_request_to_viewset(actions={'get': 'list'})
		recipes = Recipe.objects.all()
		serializer = RecipeSerializer(recipes, many=True)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_retrieve_recipe(self):
		recipe = Recipe.objects.first()
		response = self.send_request_to_viewset(actions={'get': 'retrieve'}, path_params={'pk': recipe.id})
		serializer = RecipeSerializer(recipe)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_recipe(self):
		data = {
			"user": self.authenticated_user.id,
			"title": "Lunch",
			"description": "description",
			"time_minutes": 10,
			"price": 10.10
		}
		recipes = Recipe.objects.all()
		response = self.send_request_to_viewset(actions={'post': 'create'}, data=data)

		self.assertEqual(response.data["user"], data["user"])
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_update_recipe(self):
		recipe = Recipe.objects.first()
		data = {
			"title": "Dinner"
		}
		response = self.send_request_to_viewset(actions={'patch': 'partial_update'}, path_params={'pk': recipe.id}, data=data)

		self.assertEqual(response.data["title"], data["title"])
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_delete_recipe(self):
		recipe = Recipe.objects.first()
		response = self.send_request_to_viewset(actions={'delete': 'destroy'}, path_params={'pk': recipe.id})

		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)