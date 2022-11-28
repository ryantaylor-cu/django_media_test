from testapp.models import ReportTest

def run():
    report_list = ReportTest.objects.all()
    for report in report_list:
        print(report.title, report.graph.url)
