from haystack.query import SearchQuerySet
from django.http import JsonResponse
from django.shortcuts import render


def autocomplete(request):
    q = request.GET.get('term')
    if q:
        sqs = SearchQuerySet().autocomplete(text_auto=q)
        results = [str(result.object) for result in sqs[:5]]
    else:
        results = []
    return JsonResponse(results, safe=False)


def home(request):
    return render(request, 'myapp/home.html')