from django.db import models

# Create your models here.
class Applicants(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('croissant', 'Croissant')
    ]
    NATIONALITY_CHOICES = [
        ('chinese','Chinese'),
        ('canadian', 'Canadian'),
        ('mexican', 'Mexican'),
        ('japanese', 'Japanese'),
        ('korean', 'Korean'),
        ('ghanaian', 'Ghanaian')
    ]
    first_name = models.CharField(max_length=255, null=True, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=False)
    gender = models.CharField(choices=GENDER_CHOICES, null=True, blank=False, default='other')
    date_of_birth = models.DateField(auto_now_add=True, null=True, blank=False)
    nationality = models.CharField(choices=NATIONALITY_CHOICES, null=True, blank=False)
    address = models.TextField(max_length=255, null=True, blank=False)
    phone_number = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(max_length=555, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.email} | {self.phone_number}'

class Guardians(models.Model):
    RELATIONSHIP_CHOICES = [
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('guardian', 'Guardian')
    ]
    applicant_id = models.ForeignKey(Applicants, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=False)
    relatinship = models.CharField(choices=RELATIONSHIP_CHOICES, null=True, blank=False, default='guardian')
    phone_number = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(max_length=555, null=True, blank=False)
    address = models.TextField(max_length=255, null=True, blank=False)

    def __str__(self):
        return f"{self.full_name} | {self.applicant_id}'s {self.relatinship}"

class Programs(models.Model):
    LEVEL_CATEGORIES = [
        ('easy', 'Easy'),
        ('intermediate', 'Intermediate'),
        ('hard', 'Hard'),
        ('extreme', 'Extreme')
    ]
    program_name = models.CharField(max_length=255, null=True, blank=False)
    level = models.CharField(choices=LEVEL_CATEGORIES,max_length=255, null=True, blank=False)
    academic_year = models.CharField(max_length=255, null=True, blank=False)
    capacity = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return f"{self.program_name} | {self.level} | {self.academic_year}"

class Academic_Records(models.Model):
    applicant_id = models.ForeignKey(Applicants, on_delete=models.CASCADE)
    previous_school = models.CharField(max_length=255, null=True, blank=False)
    last_class_completed = models.IntegerField(null=True, blank=False)
    grade = models.IntegerField(max_length=3, null=True, blank=False)
    completion_year = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return f"{self.previous_school} | {self.grade}"

class Admin(models.Model):
    ROLE_CHOICES = [
        ('academic facilitator', 'Academic Facilitator'),
        ('head of school', 'Head of School'),
        ('director', 'Director')
    ]
    username = models.CharField(max_length=255, null=True, blank=False)
    password = models.CharField(max_length=255, null=True, blank=False)
    full_name = models.CharField(max_length=255, null=True, blank=False)
    role = models.CharField(choices=ROLE_CHOICES,max_length=255, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=False)

    def __str__(self):
        return f"{self.username} | {self.role}"

class Applications(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('pending', 'Pending'),
        ('denied', 'Denied')
    ]
    applicant_id = models.ForeignKey(Applicants, on_delete=models.CASCADE)
    program_id = models.ForeignKey(Programs, on_delete=models.CASCADE)
    applicant_number = models.CharField(max_length=255, null=True, blank=False)
    status = models.CharField(choices=STATUS_CHOICES,max_length=255, null=True, blank=False)
    submission_date = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    reviewed_by = models.ForeignKey(Admin, on_delete=models.CASCADE)
    review_date = models.DateTimeField(auto_now_add=True, null=True, blank=False)

    def __str__(self):
        return f"{self.applicant_id} | {self.status} | {self.reviewed_by} | {self.review_date}"

