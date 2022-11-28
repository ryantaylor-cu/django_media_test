from testapp.models import ReportTest
import mysite.settings

def run():
    filename = 'questionmark.png'
    # File must be at os.path.join(settings.MEDIA_PATH, 'questionmark.png')
    report = ReportTest(title='Question Mark')
    report.graph.name = filename
    report.save()
