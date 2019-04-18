import pygal
from bugs.models import Bug
from features.models import Feature
from pygal.style import Style
from datetime import date, datetime, timedelta

################ Custom Styles ################

custom_style = Style(
    background='transparent',
    plot_background='transparent',
    foreground='#000',
    foreground_strong='#fafafa',
    foreground_subtle='#fafafa',
    opacity='.9',
    opacity_hover='1',
    colors=('#00171f', '#007ea7', '#003459'),

    value_font_size=30,
    legend_font_size=20,
    tooltip_font_size=30,
    no_data_font_size=30
)

################# Bug Charts ###################

def chart_total_bug(bug):
    """
    Calculate the total amount of bugs in
    each status, and present this on a pie chart 
    """
    status_open = bug.objects.filter(status='OPEN').count()
    status_progress = bug.objects.filter(status='IN PROGRESS').count()
    status_fixed = bug.objects.filter(status='FIXED').count()
    p_chart = pygal.Pie(print_values=True,
                        legend_at_bottom_columns=3,
                        legend_box_size=30,
                        margin=0,
                        style=custom_style
                        )

    p_chart.add('OPEN', status_open)
    p_chart.add('IN PROGRESS', status_progress)
    p_chart.add('FIXED', status_fixed)
    return p_chart.render()
    
    
def chart_by_time_bug(bug, days):
    """
    Calculate how many days each bug has been in
    each status, and display this data on a pie chart
    """
    status_open = bug.objects.filter(
        status='OPEN', open_date__gte=datetime.now() - timedelta(days=days)).count()
    status_progress = bug.objects.filter(
        status='IN PROGRESS', in_progress_date__gte=datetime.now() - timedelta(days=days)).count()
    status_fixed = bug.objects.filter(
        status='FIXED', fixed_date__gte=datetime.now() - timedelta(days=days)).count()
    p_chart = pygal.Pie(print_values=True,
                        legend_at_bottom_columns=3,
                        legend_box_size=30,
                        margin=0,
                        style=custom_style,
                        no_data_font_size=30,
                        no_data_text='No Recorded Data',
                        no_data_font_family='san-serif')

    if status_open == 0 and status_progress == 0 and status_fixed == 0:
        return 'No data has been collected for this period yet.'
    else:
        p_chart.add('OPEN', status_open)
        p_chart.add('IN PROGRESS', status_progress)
        p_chart.add('FIXED', status_fixed)
        return p_chart.render()
        
        
def BugsPieChart():
    # Displays data calculated from chart_total_bug
    chart = chart_total_bug(Bug)
    return chart
    
    
def BugsDailyStatus():
    """ 
    Displays data calculated from chart_by_time_bug,
    but within a daily period 
    """
    chart = chart_by_time_bug(Bug, 1)
    return chart


def BugsWeeklyStatus():
    """ 
    Displays data calculated from chart_by_time_bug,
    but within a weekly period 
    """
    chart = chart_by_time_bug(Bug, 7)
    return chart


def BugsMonthlyStatus():
    """ 
    Displays data calculated from chart_by_time_bug,
    but within a monthly period 
    """
    chart = chart_by_time_bug(Bug, 30)
    return chart


############# Feature Charts ################

def chart_total_feature(feature):
    """
    Calculate the total amount of features in
    each status, and present this on a pie chart 
    """
    status_incomplete = feature.objects.filter(status='INCOMPLETE').count()
    status_progress = feature.objects.filter(status='IN PROGRESS').count()
    status_complete = feature.objects.filter(status='COMPLETE').count()
    p_chart = pygal.Pie(print_values=True,
                        legend_at_bottom_columns=3,
                        legend_box_size=30,
                        margin=0,
                        style=custom_style
                        )

    p_chart.add('INCOMPLETE', status_incomplete)
    p_chart.add('IN PROGRESS', status_progress)
    p_chart.add('COMPLETE', status_complete)
    return p_chart.render()
    
    
def chart_by_time_feature(feature, days):
    """
    Calculate how many days each feature has been in
    each status, and display this data on a pie chart
    """
    status_incomplete = feature.objects.filter(
        status='INCOMPLETE', incomplete_date__gte=datetime.now() - timedelta(days=days)).count()
    status_progress = feature.objects.filter(
        status='IN PROGRESS', in_progress_date__gte=datetime.now() - timedelta(days=days)).count()
    status_complete = feature.objects.filter(
        status='COMPLETE', completed_date__gte=datetime.now() - timedelta(days=days)).count()
    p_chart = pygal.Pie(print_values=True,
                        legend_at_bottom_columns=3,
                        legend_box_size=30,
                        margin=0,
                        style=custom_style,
                        no_data_font_size=30,
                        no_data_text='No Recorded Data',
                        no_data_font_family='san-serif')

    if status_incomplete == 0 and status_progress == 0 and status_complete == 0:
        return 'No data has been collected for this period yet.'
    else:
        p_chart.add('INCOMPLETE', status_incomplete)
        p_chart.add('IN PROGRESS', status_progress)
        p_chart.add('COMPLETE', status_complete)
        return p_chart.render()
        
        
def FeaturesPieChart():
    # Displays data calculated from chart_total_feature
    chart = chart_total_feature(Feature)
    return chart