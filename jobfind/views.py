from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
# jobs/views.py
from rest_framework.views import APIView
from .models import Job
from .models import Company
from .tasks import run_company_scraper
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def JobListAPI(request):
    jobs = Job.objects.all().values()
    return Response(jobs)

@csrf_exempt
@api_view(['POST'])
def run_all_scrapers(request):
    companies = Company.objects.all()
    for company in companies:
        run_company_scraper(company)
    return Response({"message": "Scraping started for all companies"})
    
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=400)

    user = User.objects.create_user(username=username, password=password)
    return Response({"message": "User registered successfully"})


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"error": "Invalid credentials"}, status=400)

    login(request, user)  # SESSION LOGIN
    return Response({"message": "Logged in successfully"})


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out"})


@api_view(['GET'])
def check_auth(request):
    if request.user.is_authenticated:
        return Response({"authenticated": True, "username": request.user.username})
    return Response({"authenticated": False})
