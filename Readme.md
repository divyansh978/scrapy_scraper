# bbb scraper
This is a scraper of bbb.org website which use its sitemap data to scrape businesses details. This project exist just as a code sample. 

## Installation
Instructions to get your project up and running:


Steps:

1. Clone this repo in your desired folder.
2. Then create a virtual environment using below command
```bash
python3 -m venv virtualenv
```
3. Then activate that virtualenv using below command

In linux:
```bash
source virtualenv/bin/activate
```
In Windows:
```bash
virtualenv\scripts\activate
```
4. Then install all the required packages using requirements.txt file using below command

```bash
python3 -m pip install -r requirements.txt
```
5. Then import the mysql db schema in your machine's mysql server and create the .env file as described in the .env.example and replace the values with your correct values.

6. Then just start downloading the bbb.org website's sitemaps manually from this url https://www.bbb.org/sitemap-business-profiles-index.xml After downloading the first sitemap just place it in the bbb_scrapy_scraper and run the xml_to_db.py script. This script will convert the data from this sitemap file and push the rows in the database table. After inserting the first sitemap file now you are ready to run the scraper.

7. Then in your command prompt go to the directory level bbb_scrapy_scraper and run below command to start the spider
```bash
python3 -m scrapy crawl business_profiles
```
8. In the dbload.py I have put a limit of 10 records per call so after 10 companies details are fetched the scraper will stop. But you can tweak this value. Also I will recommend using a web proxy for running scrapers instead of it on bare ip.
