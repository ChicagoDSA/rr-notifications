from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import SignupForm
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('debug_logger')


@require_http_methods(["GET", "POST"])
def index(request):
    return render(request, 'accounts/index.html')



def account_signup(request):
    """Test view that allows the user to submit a form with a date and some text. 
    It will run a test "DataTask" synchronously for now  

    Arguments:
        request {request} -- Standard DJango request
    """
    logger.debug(request)
    if request.method == 'POST':
        # Code for POST requests
        form = SignupForm(request.POST)
        # check if form fields are valid
        if form.is_valid():
            data = form.cleaned_data
            logger.debug('data from form')
            logger.debug(data)
          

        # set context data after the "DataTask" runs
        submit_type = 'POST Request'
    else: 
        # Code for GET requests
        form = SignupForm()
        submit_type = 'GET Request'

        # The context is a dictionary of values you want to display in the template
        # Things like strings, models from teh DB anything you want to insert into template
    ctxt = {
        
    }
        
    return render(request, 'accounts/signup.html', ctxt)
