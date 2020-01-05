from django.shortcuts import render,redirect

from django.http import JsonResponse
# Create your views here.

from .models import Student

def index(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,'index.html',context)



def create(request):
    created=False
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        school=request.POST['school']
        description=request.POST['description']
        newstudent=Student.objects.create(name=name,age=age,school=school,description=description)
        newstudent.save()
        created=True
        if request.is_ajax():
            json_data={
                "created":created,
                "notcreated":not created,
            }
            print('hi')

            return JsonResponse(json_data)
            # return redirect('index')
    else:
        print(' something is wrong in the water')

    return render(request,'studentform.html',{})