from django.shortcuts import render
from django.core.paginator import Paginator
from homework.models import ArtiInfo

# Create your views here.
def index(request):
        limit =4
        arti= ArtiInfo.objects[:1]
        paginator = Paginator(arti,limit)
        page = request.GET.get('page',1)
        load =paginator.page(page)
        context={
                'arti':load
        }
        return render(request,'semanticwb.html',context)



