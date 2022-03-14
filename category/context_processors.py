from dataclasses import dataclass
from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

    # takes an argument request and returns dictionary in data