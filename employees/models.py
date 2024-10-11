from django.db import models

from django.conf import settings
from django.urls import reverse


class Employee(models.Model):
    POSITION_CHOICES = (
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('technical_manager', 'Technical Manager'),
        ('designer', 'Designer'),
        ('devops', 'DevOps'),
        ('project_manager', 'Project Manager'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, )
    national_code = models.CharField(max_length=10,blank=False, null=False)
    phone_number = models.CharField(max_length=12, default='09121111111',blank=False, null=False)
    position = models.CharField(choices=POSITION_CHOICES, max_length=30)
    salary = models.PositiveIntegerField()
    start_date = models.DateTimeField(auto_now_add=True)
    is_employed = models.BooleanField(default=True)

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('employee_detail', args=[self.pk])
