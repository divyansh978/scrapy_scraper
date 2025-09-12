import scrapy
import dbload
from bs4 import BeautifulSoup
from datetime import datetime

class BusinessProfilesSpider(scrapy.Spider):
    name = "business_profiles"
    start_urls=[]

    async def start(self):
        urls = dbload.fetchall()
        print(urls)
        for url in urls:
            yield scrapy.Request(url=url[0], callback=self.parse,cb_kwargs={'id':url[1]})

    def parse(self, response, id):
        soup = BeautifulSoup(response.body.decode('utf-8',errors='ignore'),'html.parser')

        data = {'business_name':'','phone':'','website':'','address':'','incorporated':'','entity_type':'','management':'','business_categories':'','sitemap_url':response.request.url,'sitemap_id':id}

        # get the business name
        business_name = soup.find(id='businessName')
        if business_name:
            data['business_name'] = business_name.text.strip()
        
        # get the business website
        container = soup.select_one('.bpr-header-contact')

        if container:
            allahrefs = container.find_all('a')

            for val in allahrefs:
                # get the website
                if 'website' in val.text.strip().lower():
                    data['website'] = val['href'].strip()

                # get the phone no.
                if 'tel' in val['href'].strip():
                    data['phone'] = val.text.strip()

        # get business address
        address_container = soup.select_one('.bpr-overview-address')
        if address_container:
            data['address'] = address_container.text.strip()

        # get all ramaining
        box = soup.select_one('.bpr-details')

        if box:
            sections = box.find_all(class_='bpr-details-dl-data')
            for section in sections:
                header = section.find('dt')
                mid = section.find('dd')

                if not header or not mid:
                    continue
                
                text = header.text.strip().lower()

                # get business incorporated date
                if 'incorporated' in text:
                    data['incorporated'] = mid.text.strip()

                # get business entity
                if 'entity' in text:
                    data['entity_type'] = mid.text.strip()

                # get management member name
                if 'management' in text :
                    data['management'] = mid.text.strip()

                # get business categories
                if 'category' in text:
                    data['categories'] = mid.text.strip()

        if data['incorporated']:
            dt = datetime.strptime(data['incorporated'],'%m/%d/%Y').date()
            data['incorporated'] = dt.strftime('%Y-%m-%d %H:%M:%S')
        
        dbload.insert(data,id)