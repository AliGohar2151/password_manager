from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PasswordEntry
from .forms import PasswordEntryForm


@login_required
def index(request):
    passwords = PasswordEntry.objects.filter(user=request.user)
    return render(request, "passwords/index.html", {"passwords": passwords})


@login_required
def add_password(request):
    if request.method == "POST":
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            password_entry = form.save(commit=False)
            password_entry.user = request.user
            password_entry.encrypt_password(password_entry.password)
            password_entry.save()
            return redirect("index")
    else:
        form = PasswordEntryForm()
    return render(request, "passwords/add_password.html", {"form": form})
