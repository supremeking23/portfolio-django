from django.shortcuts import render,get_object_or_404
from .models import Job

# Create your views here.
def home(request):
	jobs = Job.objects
	jobs_list = {'jobs':jobs}
	return render(request,'jobs/home.html',jobs_list)


def detail(request,job_id):
	job_detail = get_object_or_404(Job,pk=job_id)
	specific_job = {'job':job_detail}
	return render(request,'jobs/detail.html',specific_job)