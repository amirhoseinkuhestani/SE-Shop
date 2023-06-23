from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import *
from .forms import TicketForm,ReplyForm

def home(request):
    return render(request, "home.html", {'user': request.user})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error': 'Email or username already exists'})
            else:
                user = User.objects.create_user(phone_number=phone_number, email=email, username=username, password=password1)
                messages.success(request, 'Signup successful! You can now log in.')
                return redirect('shop:home')
        else:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('shop:home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html', {'error': ''})
    
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def logout(request):
    auth_logout(request)
    return redirect('shop:home')

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.sender = request.user
            ticket.save()
            messages.success(request, 'Ticket submitted successfully!')
            return redirect('shop:ticket_list')
    else:
        form = TicketForm()
    return render(request, 'ticket_create.html', {'form': form})

def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})

def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    replies = TicketReply.objects.filter(ticket=ticket)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.ticket = ticket
            reply.sender = request.user
            reply.save()
            messages.success(request, 'Reply submitted successfully!')
            return redirect('shop:ticket_detail', ticket_id=ticket_id)
    else:
        form = ReplyForm()
    return render(request, 'ticket_detail.html', {'ticket': ticket, 'replies': replies, 'form': form})