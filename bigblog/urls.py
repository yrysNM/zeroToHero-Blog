from django.urls import path
from . import views;

urlpatterns = [
	#post views
	path('user_login/', views.user_login, name = "user_login"),
	path('user_register/', views.register, name = "register"),
	# path('just/', views.just, name = "just"),
	# path('thanks_page/', views.thanks_page, name = "thanks_page"),		
]