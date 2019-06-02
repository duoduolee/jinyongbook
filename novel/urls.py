from django.urls import path
from . import views

urlpatterns = [
    path('', views.chapter_list, name='chapter_list'),
	path('chapter/<int:novel_id>/', views.chapter),

]
