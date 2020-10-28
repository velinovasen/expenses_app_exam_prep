from django.contrib import admin
from django.urls import path

from .views.expenses_views import create_expense_view
from .views.profile_views import home_page_view, create_profile_view

urlpatterns = [
    path('', home_page_view, name='home page'),
    path('profile/', create_profile_view, name='create profile'),
    # path('profile/edit/', edit_profile, name='edit profile'),
    # path('profile/delete/', delete_profile, name='delete profile'),
    # # expenses
    path('create/', create_expense_view, name='create expense'),
    # path('edit/<int:id>', edit_expense, name='edit expense'),
    # path('delete/<int:id>', delete_expense, name='delete expense'),
]
