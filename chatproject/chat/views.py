from django.shortcuts import render
from django.views import View


# Create your views here.


class Main(View):
    def get(self, request):
        print(request.session.get('get_me_from_consumer'))
        return render(request=request, template_name="chat/main.html")


class Login(View):
    def get(self, request):
        return render(request=request, template_name="chat/login.html")

class Register(View):
    def get(self, request):
        return render(request=request, template_name="chat/register.html")

class Logout(View):
    def get(self, request):
        return render(request=request, template_name="chat/logout.html")


class Home(View):
    def get(self, request):
        return render(request=request, template_name="chat/home.html")

class ChatPerson(View):
    def get(self, request):
        return render(request=request, template_name="chat/chat_person.html")