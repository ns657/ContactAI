from django.urls import path
from .views import contact_view, success_view

urlpatterns = [
    path('', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]
from .views import contact_view, success_view, view_submissions

urlpatterns = [
    path('', contact_view, name='contact'),
    path('success/', success_view, name='success'),
    path('submissions/', view_submissions, name='view_submissions'),
]