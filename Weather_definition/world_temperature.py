import requests as r
import requests.exceptions


your_city = input('Enter your city: ')
flag = True
params = {
    'q': your_city,
    'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
    'units': 'metric'
}
try:
    req = r.get('https://api.openweathermap.org/data/2.5/weather', params=params).json()
except requests.exceptions.ConnectionError:
    flag = False
    print('\n_____Connection error. Try again_____')
if flag:
    try:
        weather = req['weather'][0]['main']
        temperature = str(req['main']['temp']) + ' (degrees Celsius)'
        wind = str(req['wind']['speed']) + ' (meters per second)'
    except Exception:
        flag = False
        print('\n_____Incorrect city. Please, try again(((_____')
    if flag:
        print('='*63)
        print(f'|||Weather: {weather:<48}|||\n|||Temperature: {temperature:<44}|||\n|||Wind`s speed: {wind:<43}|||')
        print('='*63)