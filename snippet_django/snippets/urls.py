from django.urls import path
from .views import OverviewAPI, TagViewSet

urlpatterns = [
	# api overview
    path('overview/', OverviewAPI.as_view(), name='overview-api'),
]