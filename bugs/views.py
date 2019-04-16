from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Bug
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