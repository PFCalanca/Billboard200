import scrapy
import json
import pandas as pd

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
        scrapy.Request(url='https://www.billboard.com/charts/billboard-200/', headers=self.headers, callback=self.parse)
        df = pd.DataFrame()
        posicao = response.xpath(".//span[@class='chart-element__rank__number']/text()").extract()
        df['posicao'] = posicao
        titulo = response.xpath(".//span[starts-with(@class, 'chart-element__information__song')]/text()").extract()
        df['song_name'] = titulo
        artista = response.xpath(".//span[starts-with(@class, 'chart-element__information__artist')]/text()").extract()
        df['artista'] = artista
        pos_ultima_semana = response.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[0].extract()
        df['ultima_semana'] = pos_ultima_semana
        pico = response.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[1].extract()
        df['pico'] = pico
        semanas_no_topo = response.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[2].extract()
        df['semanas'] = semanas_no_topo
        df.to_csv (r'C:\Users\SrCal\Desktop\Aula_IA\Aula_raspagem\Projetos\Billboard200\billboard.csv', index = None, header=True)
        
        
        #if not os.path.exists(self.save_dir):
         #   os.makedirs(self.save_dir)
        #billboard = os.path.join(self.save_dir, 'billboard.csv')
        #df.to_csv(billboard, index=False)
            #print(titulo,artista,posicao,ultima_semana,pico,semanas)
            

       # except IndexError as err:
        #    print("Deu merda".format(err))
     
      #  hot200 = response.xpath("//li[starts-with(@class, 'chart-list__element')]")
        
       # titulo = response.xpath(".//span[starts-with(@class, 'chart-element__information__song')]/text()").get(),
       # artista = response.xpath(".//span[starts-with(@class, 'chart-element__information__artist')]/text()").get(),
       # posicao = response.xpath(".//span[@class='chart-element__rank__number']/text()").get(),
       # ultima_semana = response.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[0].get(),
       # pico = response.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[1].get(),
       # semanas = response.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[2].get()
      #  for hit in hits:
      #      yield {
      #          'titulo': hit.xpath(".//span[starts-with(@class, 'chart-element__information__song')]/text()").get(),
      #          'artista': hit.xpath(".//span[starts-with(@class, 'chart-element__information__artist')]/text()").get(),
      #          'posicao': hit.xpath(".//span[@class='chart-element__rank__number']/text()").get(),
      #          'ultima_semana': hit.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[0].get(),
      #          'pico': hit.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[1].get(),
       #         'semanas': hit.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[2].get()
       #     }
    #    yield 
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
