from django.shortcuts import render, redirect
from .forms import UserCommentForm
import requests
from .models import UserComment
# Create your views here.


def home(request) -> render:
    if request.method == 'POST':
        form = UserCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = UserCommentForm()

    url = 'https://api.weatherapi.com/v1/current.json'
    params = {
        'key': '<KEY>', 
        'q': 'London'
    }
    try:
        # Fetch the weather data
        response = requests.get(url, params=params)
        weather_data = response.json()  # Parse the JSON response
        
        # Aggregating weather data
        data = {
            'city': weather_data['location']['name'],
            'temperature': weather_data['current']['temp_c'],
            'condition': weather_data['current']['condition']['text'],
        }
        
    except requests.exceptions.RequestException as e:
        data = {'error': 'Could not retrieve weather data'}
    print(data)

    # fetching the top 5 comments for homepage.
    comments = UserComment.objects.all().order_by('-id')[:5]
    res = {'data':data, 'comments':comments}
    return render(request, 'home.html', res)


def allComments(request) -> render:
    comments = UserComment.objects.all().order_by('-id')
    
    return render(request, 'allCommentsPage.html', {'comments':comments})
