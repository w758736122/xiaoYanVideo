from bs4 import BeautifulSoup
import requests
import pymongo
import time

client = pymongo.MongoClient('localhost',27017)
spider = client['spider']
video_spider = spider['video_spider']

def  video(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    i=1
    try:
        while(i<30):
            data={
                'titles' : soup.select('#screening > div.screening-bd > ul > li:nth-of-type({}) > ul > li.title > a'.format(i))[0].text,
                'links' : soup.select('#screening > div.screening-bd > ul > li:nth-of-type({}) > ul > li.title > a'.format(i))[0].get('href'),
                'data_years' : soup.select('#screening > div.screening-bd > ul > li:nth-of-type({})'.format(i))[0].get('data-release'),
                'data_title' : soup.select('#screening > div.screening-bd > ul > li:nth-of-type({})'.format(i))[0].get('data-title'),
                'data_rate' : soup.select('#screening > div.screening-bd > ul > li:nth-of-type({})'.format(i))[0].get('data-rate'),
                'data_video_long' : soup.select('#screening > div.screening-bd > ul > li:nth-of-type({})'.format(i))[0].get('data-duration'),
                'data_region' : soup.select('#screening > div.screening-bd > ul > li:nth-of-type({})'.format(i))[0].get('data-region'),
                'data_director' : soup.select('#screening > div.screening-bd > ul > li:nth-of-type({})'.format(i))[0].get('data-director'),
                'data_actors' : soup.select('#screening > div.screening-bd > ul > li:nth-of-type({})'.format(i))[0].get('data-actors'),
                'img' : soup.select('#screening > div.screening-bd > ul > li:nth-of-type({}) > ul > li.poster > a > img '.format(i))[0].get('src'),
                'ticket':soup.select('#screening > div.screening-bd > ul > li:nth-of-type({}) > ul > li.ticket_btn > span > a'.format(i))[0].get('href')
            }
            i=i+1
            download(data['img'],data['data_title'])
            video_spider.insert_one(data)
            time.sleep(3)
    except IndexError:
        pass
def download(url,name):
    r=requests.get(url)
    target = '../static/images/{}.jpg'.format(name)
    with open(target,'wb')as fs:
        fs.write(r.content)
    print(name,' ok')

video('https://movie.douban.com/')

