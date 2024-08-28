from django.urls import path
from project import views

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('send_photo/', views.SendPhoto.as_view(), name='photosendler'),
]