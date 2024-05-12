from audioop import reverse

from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from myapp.models import Users


class LoginMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        target_path = [
            '/hw/fruit/buy/',
            '/hw/fruit/cart/',
        ]
        if request.path in target_path:
            try:
                user_token = request.COOKIES['user_token']
                users = Users.get_list(token=user_token)
                if not users:
                    return HttpResponse('token过期')
            except:
                return redirect(reverse('homework:login'))
