from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Bug
from .forms import ReportBugForm
import datetime

# Create your views here.
def bugs(request):
    """
    A view which displays all bugs in a table on one page
    """
    # Order bugs by amount of upvotes
    bugs_list = Bug.objects.all().order_by('-upvotes')
    
    # Pagination for bugs
    page = request.GET.get('page', 1)
    paginator = Paginator(bugs_list, 10)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
        
    return render(request, "bugs.html", {"bugs": bugs})

def bug_detail(request, id):
    """
    A view which displays details for a specific bug
    """
    bug = get_object_or_404(Bug, id=id)
    upvotes = bug.upvotes
        
    return render(request, "bug_detail.html", {
        'bug': bug,
        'upvotes': upvotes
    })
    
@login_required   
def upvote_bug(request, id):
    """
    Function which allows user to upvote a bug
    """
    # NOTE - a user is currently able to upvote a bug
    # as many times as they wish.
    # This may be fixed in future builds.
    bug = get_object_or_404(Bug, id=id)
    bug.upvotes += 1
    bug.save()
    return redirect('bug_detail', id)
    
@login_required
def report_bug(request, id=None):
    """
    A view which renders page for report_bug form. 
    User must be logged in to access this page. 
    """
    bug = get_object_or_404(Bug, id=id) if id else None
    if request.method == "POST":
        form = ReportBugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.user = request.user
            bug.save()
            return redirect(bug_detail, bug.id)
    else:
        form = ReportBugForm(instance=bug)
    return render(request, 'report_bug.html', {'form': form})