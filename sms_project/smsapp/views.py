from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import studentModel
from .forms import StudentForms


def uhome(request):
	if request.user.is_authenticated:
		data = studentModel.objects.all()
		return render(request, "home.html", {"data": data})
	else:
		return redirect("ulogin")

def create(request):
    if request.method == "POST":
        data = StudentForms(request.POST)
        if data.is_valid():
            data.save()
            msg = "Record created successfully!"
            fm = StudentForms()
            return render(request,"create.html",{"fm":fm,"msg":msg})
        else:
            msg = "check errors"
            return render(request,"create.html",{"fm":data,"msg":msg})
    else:
        fm = StudentForms()
        return render(request,"create.html",{"fm":fm})


def remove(request, id):
    st = studentModel.objects.get(rno=id)
    st.delete()
    return redirect("home")

def ulogin(request):
    if request.user.is_authenticated:
        return redirect("uhome")
    elif request.method == "POST":
        un = request.POST.get("un")
        pw = request.POST.get("pw")
        usr = authenticate(username=un,password=pw)
        if usr is None:
            return render(request,"login.html",{"msg":"invalid login"})
        else:
            login(request,usr)
            return redirect("home")
    else:
        return render(request,"login.html")

def usignup(request):
    if request.user.is_authenticated:
        return redirect("uhome")
    elif request.method == "POST":
        un = request.POST.get("un")
        pw1 = request.POST.get("pw1")
        pw2 = request.POST.get("pw2")
        if pw1 == pw2:
            try:
                usr = User.objects.get(username=un)
                return render(request,"signup.html",{"msg":"user already exists"})
            except User.DoesNotExist:
                usr = User.objects.create_user(username=un,password=pw1)
                usr.save()
                return redirect("ulogin")
        else:
            return render(request,"signup.html",{"msg":"passwords do not match"})
    else:
        return render(request,"signup.html")
      
def ulogout(request):
    logout(request)
    return redirect("ulogin")

def ucp(request):
    if not request.user.is_authenticated:
        return redirect("ulogin")
    elif request.method == "POST":
        pw1 = request.POST.get("pw1")
        pw2 = request.POST.get("pw2")
        if pw1 == pw2:
            usr = User.objects.get(username=request.user.username)
            usr.set_password(pw1)
            usr.save()
            return redirect("ulogin")
        else:
            return render(request,"cp.html",{"msg":"password did not match"})
    else:
        return render(request,"cp.html")