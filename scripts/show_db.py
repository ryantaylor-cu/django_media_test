from testapp.models import ReportTest, ImageTest

def run():
    # Get all reports
    report_list = ReportTest.objects.all()
    for report in report_list:
        # Print the title of a report
        print(report.title)
        # Print the URL for each image in the report
        for image in report.imagetest_set.all():
            print("  --> " + image.graph.url)
        print()

