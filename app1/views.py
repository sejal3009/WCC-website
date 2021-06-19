from django.shortcuts import render
from app1.models import Complaint
# Create your views here.
def index(request):
    return render(request,'app1/index.html')


def index2(request):
    if request.method == 'POST':
            first = request.POST.get('first')
            last = request.POST.get('last')
            email = request.POST.get('email')
            number = request.POST.get('number')
            date = request.POST.get('date')
            complaint_type = request.POST.get('complaint_type')
            detail_complaint = request.POST.get('detail_complaint')
            s = Complaint(first=first, last=last, email=email, number=number, Date=date, complaint_type=complaint_type, detail_complaint=detail_complaint)
            s.save()
    return render(request,'app1/complaint.html')

def login(request):
    email=request.POST.get('email')
    password = request.POST.get('password')
    if password=="abcd" and email=="abcd@gmail":
        return complaint_view(request)
    else:
        return render(request, "app1/login.html")

def complaint_view(request):
    complaint_list = Complaint.objects.all()
    print(complaint_list)
    context = {
        'complaints': complaint_list
    }
    return render(request,"app1/complaint_view.html",context)