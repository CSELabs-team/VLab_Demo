from django.shortcuts import render_to_response
from django.template.context import RequestContext

# from todo.serializer import TodoSerializer

def social_login(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})

   return render_to_response('vlablogin.html',
                             context_instance=context)
