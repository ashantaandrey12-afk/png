# dashboard/middleware.py
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

class DashboardMiddleware:
    """
    Middleware to manage login-required URL reversals and apply authentication
    checks for the dashboard app.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URL names that require the user to be logged in
        restricted_urls = [
            reverse('dashboard:children:child_list'),
            reverse('dashboard:children:add_child'),
            reverse('dashboard:staff:staff_list'),
            reverse('dashboard:attendance:attendance_list'),
            reverse('dashboard:incidentReport:incident_list'),
            reverse('dashboard:classroom:classroom_list'),
            reverse('dashboard:schedule:schedule_list'),
            reverse('dashboard:parents:parent_list'),
        ]

        if request.path in restricted_urls and not request.user.is_authenticated:
            return redirect('login')  # Or any appropriate redirect (e.g., 'login' page)

        # Return the response for all other paths
        response = self.get_response(request)
        return response
