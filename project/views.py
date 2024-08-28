from django.shortcuts import render
from django.views import View
import requests
from project.utils import send_message, send_photo


class HomeView(View):
	def get(self, request):
		return render(request, 'index.html')

	def post(self, request):
		text = request.POST.get('text')
		send_message(text)
		return render(request, 'index.html')

class SendPhoto(View):
    def get(self, request):
        return render(request, 'send_image.html')
    
    def post(self, request):
        photo = request.FILES.get('photo')
        print(photo)
        url = 'https://api.telegram.org/bot7356746562:AAEAaiLpQiHlNspctg6bmHpzW2fVqLVJf6U/sendPhoto'        
        files = {
			'photo': photo
		}
        data = {
			'chat_id': -1001689034214,
		}
        response = requests.post(url, data=data, files=files)
        print(response.status_code)
        print(response.json())
        return render(request, 'send_image.html')