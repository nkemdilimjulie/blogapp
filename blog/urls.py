from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("post_list/", views.PostListView.as_view(), name="post_list"),  # List view
    path(
        "posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"
    ),  # Detail view
]
