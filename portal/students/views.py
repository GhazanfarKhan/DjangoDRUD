from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm, CharField, DateField, TextInput, IntegerField, DateInput, Select, ChoiceField
from students.models import Student
from django.shortcuts import render, redirect, get_object_or_404

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female.')
)


# Class Based Views

class StudentList(ListView):
    model = Student


class StudentCreate(CreateView):
    model = Student
    fields = ['firstname', 'lastname', 'age', 'gender', 'joining_date']
    success_url = reverse_lazy('students:student_list')


class StudentUpdate(UpdateView):
    model = Student
    fields = ['firstname', 'lastname', 'age', 'gender', 'joining_date']
    success_url = reverse_lazy('students:student_list')


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students:student_list')


# Function Based Views


class StudentForm(ModelForm):
    firstname = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    lastname = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    age = IntegerField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Age'}))
    joining_date = DateField(widget=DateInput(attrs={'class': 'form-control', 'placeholder': 'Joining Date'}))
    gender = ChoiceField(choices=GENDER, widget=Select(attrs={'class':'form-control'}))

    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'age', 'gender', 'joining_date']


def student_list(request, template_name='students/student_list.html'):
    students = Student.objects.all()
    data = {}
    data['object_list'] = students
    return render(request, template_name, data)


def student_create(request, template_name='students/student_form.html'):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('students:student_list')
    return render(request, template_name, {'form': form})


def student_edit(request, pk, template_name='students/student_form.html'):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('students:student_list')
    return render(request, template_name, {'form': form})


def student_delete(request, pk, template_name='students/student_confirm_delete.html'):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students:student_list')
    return render(request, template_name, {'object': student})
