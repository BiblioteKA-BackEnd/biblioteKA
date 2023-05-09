from django.urls import path
from . import views

urlpatterns = [
    # path("lending/", views.LendingView.as_view()),
    path("lending/<int:pk_book>/", views.LendingDetailView.as_view())
]
