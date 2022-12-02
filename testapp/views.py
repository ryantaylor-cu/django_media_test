from datetime import datetime
from django.shortcuts import render
import mysite.settings
from .models import ReportTest, ImageTest

def index(request):
    
    context = {
        'now': datetime.now(),
        'report': ReportTest.objects.first(),
    }
    return render(request, 'testapp/index.html', context)
    return HttpResponse(html)

    
