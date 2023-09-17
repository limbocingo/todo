import os

from pypulse import Window, Aplication
from pypulse.Template import Template

# Defining aplication route
Aplication.Vars.APLICATION_PATH = os.path.dirname(os.path.abspath(__file__))

# Defining the templates and static files places
Template.TEMPLATE_PATH = os.path.join(
    Aplication.Vars.APLICATION_PATH, 'templates')
Template.STATIC_PATH = os.path.join(
    Aplication.Vars.APLICATION_PATH, 'static')

# Setting Aplications
# I you create a new aplication you need to add this here
Aplication.SetAplication('baseapp')

# BROWSER SETTINGS
APP_SETTINGS = {
    'title': 'PyPulse App',
    'debug': False,
    'debug_file_name': 'debug.log',
    'window_size_x': 375,
    'window_size_y': 718,
    'icon_path': os.path.join(
        Aplication.Vars.APLICATION_PATH, 'window_logo.ico')
}

# Initializing Browser
browser = Window.LoadBrowser(**APP_SETTINGS)
