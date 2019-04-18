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
