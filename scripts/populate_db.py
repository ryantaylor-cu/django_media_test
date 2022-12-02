from testapp.models import ReportTest, ImageTest
import mysite.settings

def run():
    # First Create a report
    r = ReportTest(title='Question Mark')
    r.save()
    
    # Then repeat this for a variable number of images:
    filename = 'questionmark.png'
    image = ImageTest(report=r)
    image.graph.name = filename
    image.save()
