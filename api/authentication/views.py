from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class LogoutView(APIView):
	"""
	It handels the application logout. 
	"""

	def post(self, request):
		try:
			refresh_token = request.data["refresh_token"]
			token = RefreshToken(refresh_token)
			token.blacklist()
			return Response(status=status.HTTP_205_RESET_CONTENT)
		except Exception as e:
			return Response(str(e), status=status.HTTP_400_BAD_REQUEST)



class LogoutAllView(APIView):
	"""
	It handels the logout from all the devices.
	"""

	def post(self, request):
		tokens = OutstandingToken.objects.filter(user=request.user)

		for token in tokens:
			BlacklistedToken.objects.get_or_create(token=token)

		return Response(status=status.HTTP_205_RESET_CONTENT)