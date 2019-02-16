from django.urls import path
from . import views

urlpatterns = [
	path('enter/', views.post_list, name = 'post_list'),
	path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
	path('post/new/', views.post_new, name = 'post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name = 'post_edit'),
	path('post/<int:pk>/delete/', views.post_delete, name = 'post_delete'),
	path('post/<int:pk>/111211211/', views.go, name = 'go'),
	path('', views.welcome, name = 'welcome'),
	# path('post/345/', views.view_other_profile, name = 'view_other_profile'),
]