from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
from .forms import NewRecord

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def records(request):
    all_records = Record.objects.all()
    return render(request, 'records.html', {'records': all_records})

@login_required(login_url='login')
def record_details(request, pk):
    record = Record.objects.get(pk=pk)
    return render(request, 'record_details.html', {'record': record})

@login_required(login_url='login')
def add_record(request):
    if request.method == 'POST':
        form = NewRecord(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Record created successfuly.')
            return redirect('records')

    else:
        form = NewRecord()
    return render(request, 'add_record.html', {'form': form})

@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(pk=pk)
    record.delete()
    messages.success(request, f'Record {record.first_name} {record.last_name} deleted successfuly.')
    return redirect('records')

@login_required(login_url='login')
def edit_record(request, pk):
    record = Record.objects.get(pk=pk)

    if request.method == 'POST':
        form = NewRecord(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, f'Record {record.first_name} {record.last_name} updated successfully.')
            return redirect('records')
    
    else:
        form = NewRecord(instance=record)


    return render(request, 'edit_record.html', {'form': form, 'pk': record.pk})



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Wellcome {username.title()}, you are logged in')
            return redirect('index')
        else:
            messages.success(request, f'Wrong username or password please try again')
            return redirect('index')
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_user(request):
    messages.success(request, f'You are logged out, Login to continue')
    logout(request)
    
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Wellcome {username.title()}, you are registered')
            return redirect('index')

    else:
        form = SignUpForm()

        return render(request, 'register.html', {'form': form})
        
    return render(request, 'register.html', {'form': form})

@login_required(login_url="login")
def profile(request):
    return render(request, 'profile.html')