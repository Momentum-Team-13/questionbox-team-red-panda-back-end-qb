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
    # admin
    path('admin/', admin.site.urls),
    # user authentication
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    # question views
    path('api/questions/', views.AddQuestionListView.as_view(), name='create_question'),
    path('api/add/question/', views.AddQuestionListView.as_view()),
    path('api/questions/<int:pk>/', views.QuestionDetailView.as_view()),
    path('api/game/<int:pk>/question/', views.QuestionListView.as_view()),
    path('api/question/<int:pk>/delete/', views.QuestionDestroyView.as_view()),
    # user views
    path('api/user/<int:pk>/question/', views.UserQuestionListView.as_view()),
    path('api/user/<int:pk>/answer/', views.UserAnswerListView.as_view()),
    # path('api/user/<int:pk>/favorite/question/', views.UserFavoriteQuestionListView.as_view()),
    # answer views
    path('api/question/<int:pk>/answer/', views.AnswerListView.as_view()),
    path('api/answer/<int:pk>/delete/', views.AnswerDestroyView.as_view()),
    # category view
    path('api/categories/', views.CategoryListView.as_view()),
    path('api/category/<int:pk>/delete/', views.CategoryDestroyView.as_view()),
    # game views
    path('api/games/', views.CreateGameView.as_view()),
    path('api/category/<int:pk>/game/', views.GamesListView.as_view()),
    path('api/add/game/', views.CreateGameView.as_view()),
    # favorite view
    # path('api/questions/<int:question_pk>/favorites/', views.CreateFavoriteQuestionView.as_view(), name='favorite_questions'),
]