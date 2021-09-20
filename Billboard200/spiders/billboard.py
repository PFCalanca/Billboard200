import scrapy
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