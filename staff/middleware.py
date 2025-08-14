from typing import Any
from django.shortcuts import redirect
from django.urls import reverse

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path in [reverse('staff:staff_list'), reverse('staff:add_staff')]:
            return redirect('login')
        response = self.get_response(request)
        return response