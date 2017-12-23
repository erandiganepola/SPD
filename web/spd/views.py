from django.http import HttpResponse, JsonResponse
from django.template import loader

from detector.spd import SPD


def index(request):
    template = loader.get_template("spd/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def compare(request):
    docs = request.POST.getlist('docs[]')
    standardize_docs = []

    for i in docs:
        standardize_docs.append(SPD.standardize(i))

    response = {
        'similarities': SPD.compare(standardize_docs)
    }
    return JsonResponse(response)


def upload_multiple_docs(request):
    files = request.FILES.getlist('file')

    standardize_docs = []
    for value in files:
        print(value)
        read_file = value.read().decode("utf-8")
        standardize_docs.append(SPD.standardize(read_file))

    template = loader.get_template("spd/index.html")
    similarities = SPD.compare_uploaded_files(standardize_docs)
    context = {
        'uniqueness': [[files[i].name, x] for i, x in enumerate(similarities)]
    }
    return HttpResponse(template.render(context, request))
