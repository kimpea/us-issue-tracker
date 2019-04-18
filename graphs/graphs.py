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