from django.shortcuts import render
import requests
# Create your views here.

def home(request):
	
	new_city = request.POST.get('search',False)


	url='http://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=0feff28e59f24064fe087c5cd9c3238d'
	
	if not new_city:
		new_city='Ahmedabad'

	city = new_city

	r = requests.get(url.format(city)).json()
	print(r)
	weathers=[]

	# i=0
	# while i<len(r['list']):
	for i in range(len(r['list'])):
		#dictionary to store city and temprature
		wh={
			'city':city,
			'description': r['list'][i]['weather'][0]['description'],
			'icon':r['list'][i]['weather'][0]['icon'],
			'temperature': r['list'][i]['main']['temp'],
			'pressure':r['list'][i]['main']['pressure'],
			'humidity':r['list'][i]['main']['humidity'],
			'wind':r['list'][i]['wind']['speed'],
			'd_t': r['list'][i]['dt_txt']
		}

			
		weathers.append(wh)
		# i+=1
	# print(weathers)

	# i=0

	date_values=''
	dates=''
	times=''
	ddate_values=''
	ddate=''
	dtime=''
	k=0
	init=True
	new_weather=[]

	for i in range(len(weathers)):
		if  init==True:
			
			new_weather.append(weathers[i])
			date_values=new_weather[k]['d_t']
			dates,times=date_values.split(' ')
			k+=1
			init=False
			 # print(new_weather)
			# print(date_values)

		else:
			ddate_values=weathers[i]['d_t']
			ddate,dtime=ddate_values.split(' ')

			if ddate!=dates:

				if dtime==times:

						
					new_weather.append(weathers[i])
					date_values=new_weather[k]['d_t']
					dates,times=date_values.split(' ')
					k+=1

	# print(new_weather)

	return render(request,'weather.html',{'new_weather':new_weather})