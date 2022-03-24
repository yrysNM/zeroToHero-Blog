from django.urls import path, re_path
from . import views;

app_name = "bigblog"
urlpatterns = [
	#post views
	path('user_login/', views.user_login, name = "user_login"),
	path('user_register/', views.register, name = "register"),
	path('blog/', views.post_list, name = "post_list"),
	path('blog/<int:pk>/edit', views.post_edit, name = "post_edit"),
	re_path(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
	#path('blog/', views.PostListView.as_view(), name = "post_list"),
	re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),

]