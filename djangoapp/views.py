from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from djangoapp.forms import ComputerForm, ComputerSearchForm, CreateUserForm
from djangoapp.models import Computer,ComputerHistory
from  django.contrib.auth import authenticate,login,logout
import csv
def home(request):
    title = "welcome to India"
    context = {'title':title}
    return render(request,'base.html',context)
@login_required(login_url='login')
def computer_entry(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully Data Saved")
            return redirect('/computer_list')
            # form = ComputerForm()
            # context = {'form':form}
            # return render(request,'computer_entry.html',context)
        else:
            return HttpResponse("missed some Value")
    else:
        form = ComputerForm()
        context = {'form':form}
        return render(request,'computer_entry.html',context)

def computer_list(request):
    queryset = Computer.objects.all()
    form = ComputerSearchForm(request.POST)
    context = {'queryset':queryset,'form':form}
    if request.method == "POST":
        queryset = Computer.objects.all().order_by('.timestamp').filter(computer_name__icontains=form['computer_name'].value(), users_name__icontains = form['users_name'].value())
        context = {'queryset':queryset,'form':form}
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Computer list.csv"'
            writer = csv.writer(response)
            writer.writerow(['COMPUTER NAME', 'IP Address', 'MAC ADDRESS','USERNAME', 'LOCATION','PRICE', 'PURCHASE DATE','TIMESTAMP'])
            instance = queryset
            for row in instance:
                  writer.writerow([row.computer_name, row.IP_address, row.MAC_address,row.users_name,row.location,row.price ,row.purchase_date, row.timestamp])
            return response
    return render(request,'computer_list.html',context)
def computer_list_update(request,pk):
    computer = Computer.objects.get(id=pk)
    form = ComputerForm(instance=computer)
    if request.method == "POST":
        form = ComputerForm(request.POST,instance=computer)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Data Saved")
            return redirect('/computer_list')
    else:
        context = {'form':form}
        return render(request,'computer_entry.html',context)

def computer_list_delete(request,pk):
    computer = Computer.objects.get(id=pk)
    computer.delete()
    return redirect('/computer_list')

def registration_view(request):
    form = CreateUserForm()
    context = {'form':form}
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            messages.success(request, "Successfully Account is Created for", username)
            return redirect('/login')
        else:
            return redirect('register')
    else:
        return render(request,'registrations.html',context)

def loginpage_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,"Username or Password Worng")
    return render(request,'loginpage.html')

def logoutpage_view(request):
    logout(request)
    return redirect('/')

def computer_history_list(request):
    title = 'Update history'
    queryset = ComputerHistory.objects.all()
    context = {
       "title": title,
       "queryset": queryset,
    }
    return render(request, "computer_history_list.html",context)


def computer_history_list_delete(request,id):
    computer = ComputerHistory.objects.get(pk=id)
    computer.delete()
    return redirect('computer_history_list')
