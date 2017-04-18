from django.shortcuts import render
from cms_users_put.models import Pages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def show(request):
    content = Pages.objects.all()
    response = "<h1>Pages:</h1>"
    for entry in content:
        response += "<br/><a href='" + entry.name + "'>" + entry.name + "</a>"
    if request.user.is_authenticated():
        response += ("<p>Logged in as: " + request.user.username +
                     ". <a href='/admin/logout/'>Logout</a></p>")
    else:
        response += "<p>Not logged in: <a href='/admin/login/'>Login</a></p>"
    return HttpResponse(response)


@csrf_exempt
def process(request, resource):
    if request.method == "GET":
        try:
            entry = Pages.objects.get(name=resource)
            response = Pages.page
        except Pages.DoesNotExist:
            return HttpResponse("Content not found", status=404)
    elif request.method == "PUT":
        if request.user.is_authenticated():
            pagina = Pages(name=resource, page=request.body)
            pagina.save()
            response = "<h1>Se ha creado la página " + nombre + "</h1>"
        else:
            response = ("<h1>Necesitas <a href='/admin/login/'>" +
                        "hacer login</a></h1>")
    else:
        return HttpResponse("Method not allowed", status=405)
    if request.user.is_authenticated():
        response += ("<p>Logged in as: " + request.user.username +
                     ". <a href='/admin/logout/'>Logout</a></p>")
    else:
        response += "<p>Not logged in: <a href='/admin/login/'>Login</a></p>"
    return HttpResponse(response)
