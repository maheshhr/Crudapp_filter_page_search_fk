from django.shortcuts import render, redirect
from department.forms import DepartmentForm
from department.models import Department


# Create your views here.
def home(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showdept')
            except:
                pass
    else:
        form = DepartmentForm()
    return render(request, 'indexdept.html', {'form': form})


def show(request):
    departments = Department.objects.all()
    return render(request, "showdept.html", {'departments': departments})


def edit(request, id):
    department = Department.objects.get(id=id)
    return render(request, 'editdept.html', {'department': department})


def update(request, id):
    department = Department.objects.get(id=id)
    form = DepartmentForm(request.POST, instance=department)
    if form.is_valid():
        form.save()
        return redirect("/showdept")
    return render(request, 'editdept.html', {'department':department})


def destroy(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    return redirect("/showdept")
