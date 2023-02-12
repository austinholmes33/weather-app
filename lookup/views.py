from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=84737&distance=25&API_KEY=DE498CEF-FB66-4A75-9587-61637222FD57")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error"


    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})