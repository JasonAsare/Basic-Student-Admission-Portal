from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ApplicantView(ModelViewSet):
    queryset = Applicants.objects.all()
    serializer_class = ApplicantSerializer

class GuardianView(ModelViewSet):
    queryset = Guardians.objects.all()
    serializer_class = GuardianSerializer

class ProgramView(ModelViewSet):
    queryset = Programs.objects.all()
    serializer_class = ProgramSerializer

class AcademicRecordView(ModelViewSet):
    queryset = Academic_Records.objects.all()
    serializer_class = AcademicRecordSerializer

class AdminView(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class ApplicationView(ModelViewSet):
    queryset = Applications.objects.all()
    serializer_class = ApplicationSerializer