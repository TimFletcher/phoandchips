from django.shortcuts import render_to_response
from django.template import RequestContext

def server_error(request, template_name='500.html'):

    """ Custom 500 error handler to use RequestContext """
    
    return render_to_response(template_name,
        context_instance = RequestContext(request)
    )