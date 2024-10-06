from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render

from .models import Notion


def notion_list(request):
    notions = Notion.active.all()
    return render(request, "notion/notion_list.html", context={"notions": notions})

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>This page is not found</h1")
