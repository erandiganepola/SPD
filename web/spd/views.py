from django.http import HttpResponse, JsonResponse
from django.template import loader

from detector.spd import SPD


def index(request):
    template = loader.get_template("spd/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def compare(request):
    docs = request.POST.getlist('docs[]')

    response = {
        'similarities': SPD.compare(docs)
    }
    return JsonResponse(response)
