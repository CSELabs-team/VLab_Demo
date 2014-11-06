from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import logout

def panel_index(request):
    """
    Panel main page view function.
    Check if the request is from User or Administrator:
        If is_user: show available virtual machines
        If is_admin: show overall status of virtual machines
    """

    # authentication:
    if not hasattr(request.user, 'email'):
		return redirect('http://127.0.0.1:8000')

    user_email = request.user.email
    user = User.objects.filter(username=request.user.username, email=user_email)

    template = loader.get_template('panel_base.html')

    context = RequestContext(request, {
        'username': request.user.username,
        'user_email': request.user.email,
    })

    return HttpResponse(template.render(context))


# TODO: Write Functions for calling Virtual Machine APIs here:
