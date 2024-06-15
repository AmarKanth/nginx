from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate, APIRequestFactory

class APIViewRequestFactory(TestCase):
	"""
	It direclty makes the call to view.
	"""
	view_name = None
	authenticated_user = None

	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.authenticated_user = User.objects.create_user(username="amarkanth", password="password")

	@classmethod
	def tearDownClass(cls):
		User.objects.all().delete()
		super().tearDownClass()

	def send_request_to_viewset(self, actions, path_params={}, data=None, *args, **kwargs):
		factory = APIRequestFactory()
		view = self.view_name.as_view(actions)
		method = list(actions.keys())[0]

		request = getattr(factory, method)("/fake_url/", data)
		force_authenticate(request, user=self.authenticated_user)
		response = view(request, **path_params)
		return response