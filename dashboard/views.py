from django.shortcuts import render, HttpResponseRedirect
from children.models import Child
from attendance.models import Attendance
from incidentReport.models import IncidentReport
from staff.models import Staff
from classroom.models import Classroom
from schedule.models import Schedule
from parents.models import ParentGuardian
from datetime import datetime
from collections import Counter
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def dashboard_home(request):
    children_count = Child.objects.count()
    staff_count = Staff.objects.count()
    classroom_count = Classroom.objects.count()
    attendance_count = Attendance.objects.count()
    incident_count = IncidentReport.objects.count()

    # Get the count of children, incidents from the past 3 months (or another period)
    current_month = datetime.now().month
    children_this_month = Child.objects.filter(created_at__month=current_month).count()
    incidents_this_month = IncidentReport.objects.filter(date__month=current_month).count()

    # Calculate the increase or decrease
    previous_month_children = Child.objects.filter(created_at__month=current_month-1).count()
    previous_month_incidents = IncidentReport.objects.filter(date__month=current_month-1).count()

    children_increase = children_this_month - previous_month_children
    incidents_increase = incidents_this_month - previous_month_incidents

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    context = {
        'children_count': children_count,
        'staff_count': staff_count,
        'classroom_count': classroom_count,
        'attendance_count': attendance_count,
        'incident_count': incident_count,
        'children_increase': children_increase,
        'incidents_increase': incidents_increase,
        'months': months,
    }
    return render(request, 'dashboard_home.html', context)

def analytics_view(request):
    # Fetch data for child and staff analytics
    total_children = Child.objects.count()
    total_staff = Staff.objects.count()
    
    # Attendance statistics (assuming you have attendance model data)
    attendance_counts = Child.objects.values('attendance').annotate(count=Counter('attendance'))
    
    # Prepare data for the charts
    labels = ['Present', 'Absent']  # Example labels for attendance
    attendance_data = [attendance_counts.filter(attendance=True).count(), attendance_counts.filter(attendance=False).count()]
    
    return render(request, 'dashboard/analytics.html', {
        'total_children': total_children,
        'total_staff': total_staff,
        'attendance_labels': labels,
        'attendance_data': attendance_data
    })

def settings_view(request):
    if request.method == 'POST':
        if 'dark_mode' in request.POST:
            print('Dark mode enabled')
        return HttpResponseRedirect(request.path)

    return render(request, 'settings.html')
