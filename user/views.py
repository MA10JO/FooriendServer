import json

from .models import Account

from django.views import View
from django.http import JsonResponse, HttpResponse


# Create your views here.

# 회원 가입
class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email=data['email']).exists():  # 존재하는 이메일인지 확인
                return HttpResponse(status=400)

            Account(
                email=data['email'],
                password=data['password']
            ).save()

            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)


# 로그인
class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if Account.objects.filter(email=data['email']).exists():
                user = Account.objects.get(email=data['email'])
                # 사이 줄 띄움
                if user.password == data['password']:
                    return HttpResponse(status=200)

                return HttpResponse(status=401)

                return HttpResponse(status=400)

        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)

