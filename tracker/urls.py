from django.contrib import admin
from django.urls import path

from .views.expenses_views import create_expense_view, edit_expense_view, delete_expense_view
from .views.profile_views import home_page_view, create_profile_view, edit_profile_view, delete_profile_view

urlpatterns = [
    path('', home_page_view, name='home page'),
    path('profile/', create_profile_view, name='create profile'),
    path('profile/edit/', edit_profile_view, name='edit profile'),
    path('profile/delete/', delete_profile_view, name='delete profile'),
    # # expenses
    path('create/', create_expense_view, name='create expense'),
    path('edit/<int:my_id>/', edit_expense_view, name='edit expense'),
    path('delete/<int:my_id>/', delete_expense_view, name='delete expense'),
]
