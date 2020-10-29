from django.shortcuts import render, redirect

from tracker.forms import ExpenseForm, DisabledExpenseForm
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


def edit_expense_view(request, my_id):
    expense = Expense.objects.get(pk=my_id)
    context = {"form": ExpenseForm(instance=expense)}
    if request.GET:

        return render(request, 'expense-edit.html', context)
    else:
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')
        return render(request, 'expense-edit.html', context)


def delete_expense_view(request, my_id):
    expense = Expense.objects.get(pk=my_id)
    form = DisabledExpenseForm(instance=expense)
    context = {"form": form}
    if request.POST:
        expense.delete()
        return redirect('home page')
    else:
        return render(request, 'expense-delete.html', context)
