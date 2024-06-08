from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.authentication import JWTAuthentication as JWTA

class JWTAuthentication(JWTA):
	"""
	This custom wrapper skip all the public urls from authentication.
	"""

	def authenticate(self, request):
		skip_urls = ['/api/docs/', '/api/schema/']

		if request.path in skip_urls:
			return (AnonymousUser, None)

		header = self.get_header(request)
		raw_token = self.get_raw_token(header)
		validated_token = self.get_validated_token(raw_token)

		return self.get_user(validated_token), validated_token