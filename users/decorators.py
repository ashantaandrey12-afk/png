from django.http import HttpResponseForbidden

def role_required(allowed_roles):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role in allowed_roles:  # Customize role check logic
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You do not have access to this view.")
        return _wrapped_view
    return decorator
