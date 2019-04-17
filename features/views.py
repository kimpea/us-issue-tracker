from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Feature, FeatureComments
from .forms import RequestFeatureForm, FeatureCommentForm
import datetime

# Create your views here.
def features(request):
    """
    A view which displays all requested features in one page,
    and also displays graphs 
    """
    # Order features by amount of upvotes
    features_list = Feature.objects.all().order_by('-upvotes')
    
    # Pagination for features
    page = request.GET.get('page', 1)
    paginator = Paginator(features_list, 10)
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
    return render(request, "features.html", {"features": features})
    
    
def feature_detail(request, id):
    """
    A view which displays the details for a specific feature
    """
    feature = get_object_or_404(Feature, id=id)
    upvotes = feature.upvotes
    
    # Pagination for comments
    comments = FeatureComments.objects.filter(feature=id).order_by('date_created')
    comments_count = comments.count()
    comment_form = FeatureCommentForm()
    page = request.GET.get('page', 1)
    paginator = Paginator(comments, 5)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
        
    return render(request, "feature_detail.html", {
        'feature': feature,
        'upvotes': upvotes,
        'comment_form': comment_form, 
        'comments': comments,
        'comments_count': comments_count,
    })