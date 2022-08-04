from django.shortcuts import render
import requests
#Create your views here. 

def index(request):

    if request.method=="POST":
        city = request.POST['city_name']
    else:
        city = "Ashta"

    Url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f86253b429f52878636d219cba07250a'
    
    data = requests.get(Url).json()
    Temp = int(data['main']['temp']-273)

    payload = {'city':data['name'],'weather':data['weather'][0]['main'],'Desc':data['weather'][0]['description'],'Icon':'http://openweathermap.org/img/w/'+ data['weather'][0]['icon'] + '.png','Temp':Temp}

    return render(request,'mainpage.html',{'payload':payload})