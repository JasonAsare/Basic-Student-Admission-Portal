from rest_framework.serializers import ModelSerializer
from .models import *

class ApplicantSerializer(ModelSerializer):
    class Meta:
        model = Applicants
        fields = '__all__'

class GuardianSerializer(ModelSerializer):
    class Meta:
        model = Guardians
        fields = '__all__'

class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Programs
        fields = '__all__'

class AcademicRecordSerializer(ModelSerializer):
    class Meta:
        model = Academic_Records
        fields = '__all__'

class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Applications
        fields = '__all__'