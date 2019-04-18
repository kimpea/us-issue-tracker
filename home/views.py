from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from .models import Question
from .forms import FAQForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    """ A view that renders the index page """
    return render(request, "index.html")
    
def faq(request, id=None):
    """ A view that renders the FAQ page with the FAQForm """
    question = get_object_or_404(Question, id=id) if id else None
    if request.method == "POST":
        form = FAQForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            messages.success(request, "Your question has been submitted successfully")
            question.save()
            return redirect(faq)
    else:
        form = FAQForm(instance=question)
    return render(request, "faq.html", {'form': form})