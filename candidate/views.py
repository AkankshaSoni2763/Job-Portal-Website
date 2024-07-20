from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from hr.models import JobPost , CandidateApplications , SelectCandidateJob
# from candidate.models import MyApplyJobList
from candidate.models import IsSortList , MyApplyJobList
from hr.views import *
# from datetime import date
# Create your views here.

@login_required
def caHome(request):
    jobpost = JobPost.objects.all()

    print(jobpost)
    return render(request,'candidate/dashboradh.html',{'jobpost':jobpost})

@login_required
def myJob(request):
    # pass
    joblist = MyApplyJobList.objects.filter(user=request.user)
    print( joblist)
    return render(request,'candidate/myjoblist.html',{'joblist':joblist})


def applyJob(request, id):

    if request.method == 'POST':
        # Retrieving form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        college = request.POST.get('college')
        passing_year = request.POST.get('passing_year')
        yearOfExperience = request.POST.get('yearOfExperience')
        resume = request.FILES.get('resume')
        
        # Retrieving the job post object
        job = JobPost.objects.get(id=id)
        
        # Checking if the candidate has already applied for this job
        if CandidateApplications.objects.filter(user=request.user, job=job).exists():
            return redirect('dash')  # Redirecting to dashboard if already applied
        
        job.applyCount=job.applyCount+1
        job.save()
        # Creating and saving a new instance for CandidateApplications model
        candidate_application = CandidateApplications.objects.create(
            user=request.user,
            job=job,
            passingYear=passing_year,
            yearOfExperience=yearOfExperience,
            resume=resume
        )
        
        # Creating and saving a new instance for MyApplyJobList model
        my_apply_job_list = MyApplyJobList.objects.create(
            user=request.user,
            job=candidate_application
        )

        return redirect('dash') 
    
    return render(request,'candidate/apply.html')


# def joblist(request):
#     today = date.today()
#     # Your other view logic here
#     return render(request, 'myjoblist.html', {'today': today, 'jobpost': jobpost})

