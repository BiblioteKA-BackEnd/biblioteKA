from django.urls import path
from . import views

urlpatterns = [
    path("lending/", views.LendingView.as_view())
]
