from django.http import HttpResponse, JsonResponse
from django.template import loader

from detector.spd import SPD


def index(request):
    template = loader.get_template("spd/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def compare(request):
    data = request.POST
    print(data)
    doc1 = data['doc1']
    doc2 = data['doc2']
    doc1 = SPD.standardize(doc1)
    doc2 = SPD.standardize(doc2)

    response = {
        'similarities': SPD.compare([doc1, doc2])
    }
    return JsonResponse(response)
