from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Feature, FeatureComments
from .forms import RequestFeatureForm, FeatureCommentForm
from graphs.graphs import FeaturesTotalChart, FeaturesDailyStatus, FeaturesWeeklyStatus, FeaturesMonthlyStatus
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
        
    # Display graphs
    chart_total_feature = FeaturesTotalChart()    
    chart_feature_daily = FeaturesDailyStatus()
    chart_feature_weekly = FeaturesWeeklyStatus()
    chart_feature_monthly = FeaturesMonthlyStatus()
    
    return render(request, "features.html", {
        "features": features,
        'chart_total_feature': chart_total_feature,
        'chart_feature_daily': chart_feature_daily,
        'chart_feature_weekly': chart_feature_weekly,
        'chart_feature_monthly': chart_feature_monthly
    })
    
    
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
    
    
@login_required
def feature_comment(request, id=id):
    """Saves a posted comment  """
    feature = get_object_or_404(Feature, id=id)
    comment_form = FeatureCommentForm(request.POST, request.FILES)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.feature = feature
        comment_form.save()
    return redirect(feature_detail, id)
    
    
@login_required
def request_feature(request, id=None):
    """
    A view which renders page for request_feature form. 
    User must be logged in to access this page. 
    """
    feature = get_object_or_404(Feature, id=id) if id else None
    
    if request.method == "POST":
        form = RequestFeatureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.user = request.user
            feature.save()
            return redirect(feature_detail, feature.id)
    else:
        form = RequestFeatureForm(instance=feature)
        
    return render(request, 'request_feature.html', {'form': form})