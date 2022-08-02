"""question_box_BE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from question_box import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/questions/', views.QuestionListView.as_view(), name='create_question'),
    path('api/game/<int:pk>/question/', views.QuestionListView.as_view()),
    path('api/questions/', views.QuestionListView.as_view()),
    path('api/questions/<int:pk>/', views.QuestionDetailView.as_view()),
    path('api/add/question/', views.QuestionListView.as_view()),
    path('api/question/<int:pk>/answer/', views.AnswerListView.as_view()),
    path('api/games/', views.GamesListView.as_view()),
    path('api/categories/', views.CategoryListView.as_view()),
    path('api/category/<int:pk>/game/', views.GamesListView.as_view()),
]
