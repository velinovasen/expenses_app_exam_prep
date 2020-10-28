from django.shortcuts import render, redirect

from tracker.forms import ExpenseForm
from tracker.models import Expense
# Create your views here.


def create_expense_view(request):
    form = ExpenseForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home page')   # HERE WE PUT THE NAME FROM URLS.PY
    context = {
        "form": form
    }
    return render(request, 'expense-create.html', context)


def edit_expense_view():
    pass


def delete_expense_view():
    pass

