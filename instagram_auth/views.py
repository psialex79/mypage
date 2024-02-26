from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import urllib.parse

def instagram_login(request):
    client_id = '404078358940539'
    redirect_uri = 'http://45.87.247.64/instagram-auth/callback/'
    scope = 'user_profile,user_media'
    auth_url = f"https://api.instagram.com/oauth/authorize?client_id={client_id}&redirect_uri={urllib.parse.quote_plus(redirect_uri)}&scope={scope}&response_type=code"
    
    return redirect(auth_url)

def instagram_callback(request):
    code = request.GET.get('code')
    if code:
        client_id = '404078358940539'
        client_secret = 'b1543bbd8b2725aa026861a002aa4320'
        redirect_uri = 'http://45.87.247.64/instagram-auth/callback/'
        token_url = 'https://api.instagram.com/oauth/access_token'
        
        # Обмен кода на токен доступа
        payload = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'code': code
        }
        response = requests.post(token_url, data=payload)
        
        if response.status_code == 200:
            # Здесь можно обработать данные пользователя, используя токен доступа
            access_token = response.json()['access_token']
            user_info = response.json()['user']
            # Например, вывести приветствие с именем пользователя
            return HttpResponse(f"Привет, {user_info['username']}! Твой токен доступа: {access_token}")
        else:
            return HttpResponse("Ошибка получения токена доступа.")
    else:
        return HttpResponse("Ошибка аутентификации. Код доступа не получен.")
