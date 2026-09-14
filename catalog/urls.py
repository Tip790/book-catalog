from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_list.as_view(), name='book_list'),
    path("publishers/", views.publisher_list.as_view(), name='publisher_list'),
    path("reviews/", views.review_list.as_view(), name='review_list'),
]