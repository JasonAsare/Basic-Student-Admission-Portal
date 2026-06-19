from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('Applicant', ApplicantView)
routers.register('Guardian', GuardianView)
routers.register('Program', ProgramView)
routers.register('Academic Record', AcademicRecordView)
routers.register('Admin', AdminView)
routers.register('Application', ApplicationView)

urlpatterns = [
    path('api/', include(routers.urls))
]