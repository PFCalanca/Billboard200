import scrapy
import time
from datetime import date, datetime, timedelta

class BillboardSpider(scrapy.Spider):
    name = 'billboard'
    allowed_domains = ['https://www.billboard.com']
    start_urls = ['https://www.billboard.com/charts/billboard-200/']
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)
    
    
    def parse(self, response):
     
        hits = response.xpath("//li[starts-with(@class, 'chart-list__element')]")
        for hit in hits:

            posicao = response.xpath(".//span[@class='chart-element__rank__number']/text()").get(),
            titulo = response.xpath(".//span[starts-with(@class, 'chart-element__information__song')]/text()").get(),
            artista = response.xpath(".//span[starts-with(@class, 'chart-element__information__artist')]/text()").get(),
            ultima_semana = response.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[0].get(),
            pico = response.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[1].get(),
            semanas = response.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[2].get()
            print(titulo,artista,posicao,ultima_semana,pico,semanas)
     

     
     
      #  hot200 = response.xpath("//li[starts-with(@class, 'chart-list__element')]")
        
       # titulo = response.xpath(".//span[starts-with(@class, 'chart-element__information__song')]/text()").get(),
       # artista = response.xpath(".//span[starts-with(@class, 'chart-element__information__artist')]/text()").get(),
       # posicao = response.xpath(".//span[@class='chart-element__rank__number']/text()").get(),
       # ultima_semana = response.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[0].get(),
       # pico = response.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[1].get(),
       # semanas = response.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[2].get()
    
      #  yield {   
       #     'titulo': titulo,
       #     'artista' :artista,
       #     'posicao':posicao,
       #     'ultima_semana' :ultima_semana,
       #     'pico': pico,
       #     'semanas' :semanas
       # }
         
          
          
          #  yield {
           #     'titulo' : musica.xpath(".//span[starts-with(@class, 'chart-element__information__song')]/text()").get(),
            #    'artista' : musica.xpath(".//span[starts-with(@class, 'chart-element__information__artist')]/text()").get(),
             #   'posicao' : musica.xpath(".//span[@class='chart-element__rank__number']/text()").get(),
              #  'ultima_semana' : musica.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[0].get(),
              #  'pico' : musica.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[1].get(),
              #  'semanas' : musica.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[2].get()
           # }
