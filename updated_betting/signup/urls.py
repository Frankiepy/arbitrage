from django.urls import path
from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    # Add other URL patterns as needed
]
