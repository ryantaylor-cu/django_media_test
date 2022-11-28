from datetime import datetime
from django.shortcuts import render
import mysite.settings
from .models import ReportTest

def index(request):
    
    context = {
        'now': datetime.now(),
        'report_list': ReportTest.objects.all(),
    }
    return render(request, 'testapp/index.html', context)
    return HttpResponse(html)

    
