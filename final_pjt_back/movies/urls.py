from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.movie_all),
    path('list/', views.movie_list),
    path('genres/', views.movie_genres),
    path('recommended/', views.movie_recommended),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/', views.review_create),
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('reviews/<int:review_pk>/comments/', views.comment_create),
    path('comments/', views.comment_list),
]
