from django.shortcuts import render, redirect
from tracker.forms import ProfileForm
from tracker.models import Profile, Expense


# Create your views here.


def home_page_view(request):
    my_form = ProfileForm()
    context = {"form": my_form}
    if Profile.objects.exists():
        profile = Profile.objects.all()[0]
        expenses = Expense.objects.all()
        sum_left = profile.budget - sum([x.price for x in expenses])
        context = {
            "sum_left": sum_left,
            "profile": profile,
            "expenses": expenses,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return render(request, 'home-no-profile.html', context)


def create_profile_view(request):
    if Profile.objects.exists():
        profile = Profile.objects.all()[0]
        expenses = Expense.objects.all()
        sum_left = profile.budget - sum([x.price for x in expenses])
        context = {
            "profile": profile,
            "sum_left": sum_left
        }
        return render(request, 'profile.html', context)

    if request.GET:
        context = {
            "form": ProfileForm()
        }
        return render(request, 'home-no-profile.html', context)
    if request.POST:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {
            "form": form
        }
        return render(request, 'home-no-profile.html', context)

    return render(request, 'home-with-profile.html')


def edit_profile_view(request):
    profile = Profile.objects.all()[0]
    context = {
        "form": ProfileForm(instance=profile)
    }
    if request.POST:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

        return render(request, 'profile-edit.html', context)
    return render(request, 'profile-edit.html', context)


def delete_profile_view(request):
    expenses = Expense.objects.all()
    profile = Profile.objects.all()
    if request.POST:
        expenses.delete()
        profile.delete()
        return redirect('home page')
    return render(request, 'profile-delete.html')

