from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views


router = DefaultRouter()
router.register('', views.RecipeViewset)

urlpatterns = [
	path('recipe/', include(router.urls)),
]