from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.
def home(request):
	form = StudentForm()
	students = Student.objects.all()
	return render(request, 'testapp/home.html', {'form':form, 'students':students})

def save_data(request):
	if request.method == "POST":
		stuid = request.POST.get('stuid')
		name = request.POST.get('name')
		rollno = request.POST.get('rollno')
		course = request.POST.get('course')
		if(stuid == ''):
			data = Student(name=name, rollno=rollno, course=course)
		else:
			data = Student(id=stuid, name=name, rollno=rollno, course=course)
		data.save()
		students = Student.objects.all()
		html = render_to_string("testapp/student.html", context={'students':students})
		return JsonResponse({'status':200, 'html':html})
	else:
		return JsonResponse({'status':400})

def delete_data(request):
	if request.method == "POST":
		id = request.POST.get("id")
		obj = Student.objects.get(pk=id)
		obj.delete()
		# students = Student.objects.all()
		# html = render_to_string("testapp/student.html", context={'students':students})
		# return JsonResponse({'status':200, 'html':html})
		return JsonResponse({'status':200})
	else:
		return JsonResponse({'status':400})

def edit_data(request):
	if request.method == "POST":
		id = request.POST.get("id")
		student = Student.objects.get(pk=id)
		student_data = {'id':student.id, 'name':student.name, 'rollno':student.rollno, 'course':student.course}
		return JsonResponse(student_data)
	else:
		return JsonResponse({'status':400})


