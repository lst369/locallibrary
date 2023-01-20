from django.urls import path
from . import views
from django.urls import include, re_path

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(),
            name='book-detail'),
]
