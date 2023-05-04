from django.urls import path

from . import views

urlpatterns = [
    path("follows/<int:pk_book>/", views.FollowView.as_view()),
    path("follows/<int:pk_follow>/", views.FollowDetailedView.as_view()),
]
