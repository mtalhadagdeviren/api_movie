import requests
import json


def nowPlayingMovie():
    url='https://api.themoviedb.org/3/movie/now_playing?api_key=f89e6957ccdd82364dc319fa9abd303a&language=en-US&page=1'
    response = requests.request("GET", url)
    result=json.loads(response.text)
    for i in result['results']:
        print('-' + i['original_title'])

def topratedMovie():
    url='https://api.themoviedb.org/3/movie/top_rated?api_key=f89e6957ccdd82364dc319fa9abd303a&language=en-US&page=1'
    response = requests.request("GET", url)
    result=json.loads(response.text)
    for i in result['results']:
        print('-' + i['original_title'])

def movieSearch(search):
    url=f'https://api.themoviedb.org/3/search/movie?api_key=f89e6957ccdd82364dc319fa9abd303a&language=en-US&query={search}&page=1&include_adult=false'
    response = requests.request("GET", url)
    result=json.loads(response.text)
    for i in result['results']:
        print('-' + i['original_title'])
    
    

while True:
    choice=input('1- Vizyondaki Filmler\n2- En Popüler Filmler\n3- Arama\n4- Çıkış\n')
    if(choice == '4'):
        break
    else:
        if(choice == '1'):
            nowPlayingMovie()
        elif(choice == '2'):
            topratedMovie()
        elif(choice == '3'):
            search=(input('Aranılacak Kelime: '))
            movieSearch(search)
        else:
            print('Hatalı seçim yaptınız.')