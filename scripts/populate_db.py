from testapp.models import ReportTest

def run():
    report = ReportTest(title='Question Mark')
    report.graph.name = 'questionmark.png'
    report.save()
