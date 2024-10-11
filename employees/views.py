from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployeeForm, UploadFileForm
from .models import *
from django.contrib.auth.decorators import user_passes_test

class EmployeeListView(generic.ListView):
    queryset = Employee.objects.select_related('user').all()
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'


class EmployeeDetailView(generic.DetailView):
    queryset = Employee.objects.select_related('user').all()
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'


class EmployeeCreateView(UserPassesTestMixin, generic.CreateView):
    form_class = EmployeeForm
    template_name = 'employees/employee_create.html'

    def test_func(self):
        return self.request.user.is_staff


class EmployeeUpdateView(UserPassesTestMixin, generic.UpdateView):
    form_class = EmployeeForm
    model = Employee
    template_name = 'employees/employee_create.html'

    def test_func(self):
        return self.request.user.is_staff


class EmployeeDeleteView(UserPassesTestMixin, generic.DeleteView):
    model = Employee
    template_name = 'employees/employee_delete.html'
    success_url = reverse_lazy('employee_list')

    def test_func(self):
        return self.request.user.is_staff


@user_passes_test(lambda user: user.is_staff)
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            for _, row in df.iterrows():
                employee, created = Employee.objects.get_or_create(
                    user=row['User'],
                    national_code=row['National_Code'],
                    phone_number=row['Phone_Number'],
                    position=row['Position'],
                    salary=row['Salary'],
                    is_employed=row['Is_Employed'],
                )
                if created:
                    messages.success(request, f'Successfully imported {employee.user}')
                else:
                    messages.warning(request, f'{employee.user} already exists')
            return redirect('employee_list')
    else:
        form = UploadFileForm()
    return render(request, 'employees/upload.html', {'form': form})
