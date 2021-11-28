from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from employee.forms import EmployeeForm
from employee.models import Employee


# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    employees = paginator.get_page(page_number)
    return render(request, "show.html", {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")


def search_data(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        employ = Employee.objects.filter( dept_name__dept_name__contains=searched)
        return render(request, "search.html", {'searched':searched,'employ':employ})
    else:
        return render(request, "search.html", {})
