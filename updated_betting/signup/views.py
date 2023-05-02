from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Change 'home' to the URL name of your home page
    else:
        form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})
