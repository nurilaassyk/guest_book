from django.urls import path
from webapp.views.base import home_view
from webapp.views.book_view import add_view, update_view, delete_view, confirm_delete

urlpatterns = [
    path("", home_view, name='home_view'),
    path('add/', add_view, name='add_view'),
    path('book/<int:id>/update/', update_view, name='update'),
    path("book/<int:id>/delete/", delete_view, name='delete'),
    path("book/<int:id>/confirm_delete/", confirm_delete, name='confirm_delete'),
]
