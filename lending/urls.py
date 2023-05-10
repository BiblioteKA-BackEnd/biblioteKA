from django.urls import path
from . import views

urlpatterns = [
    path("lending/<int:pk_book>/<int:pk_user>/create/", views.LendingDetailViewCreate.as_view()),
    path("lending/<int:pk_user>/list/", views.LendingDetailViewList.as_view()),
    path("lending/<int:pk_lending>/delete/", views.LendingDetailViewDestroy.as_view()),
]
