import os

from rest_framework.views import APIView
from rest_framework.response import Response

class MySiteInfo(APIView):
	def get(self, request):
		app_id = os.environ.get("APPID")
		return Response({"data":f"APPID is {app_id}"})