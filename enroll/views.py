from django.shortcuts import render
from .forms import UserRegistration
from .models import User
from django.http import JsonResponse

# from django.views.decorators.csrf import csrf_exempt
def home(request):
    form=UserRegistration()
    stud=User.objects.all()
    return render(request,'enroll/home.html ',{'form':form,'user':stud})
# Create your views here.
# @csrf_exempt
def savedata(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            uid = request.POST.get('userid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            
            if uid == '':
                usr = User(name=name, email=email, password=password)
            else:
                usr = User(id=uid, name=name, email=email, password=password)
            
            usr.save()
            stud = User.objects.values()
            user_data = list(stud)
            return JsonResponse({"status": 'Save', 'user_data': user_data})
        else: 
            return JsonResponse({'status': 0})
    else: 
        return JsonResponse({'status': 1})

def deletedata(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        
       # print(id)
        
        pi=User.objects.get(pk=id)
        
        pi.delete()
        
        
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
    
    
    
def editdata(request):
    if request.method=="POST":
        # print("ch1")
        id=request.POST.get('sid')
        print(id)
        user=User.objects.get(pk=id)
        user_data={"id":user.id,"name":user.name,"email":user.email,"password":user.password}
    return JsonResponse(user_data)

 

   
       
        
    