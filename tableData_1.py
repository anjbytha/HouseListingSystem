import requests
from bs4 import BeautifulSoup

#Name of file: tableData_1
#Group members: Anjana Bytha | abytha@andrew.cmu.edu
#               Prajakta Wani | pwani@andrew.cmu.edu
#               Rahul Goenka | rgoenka@andrew.cmu.edu
#               Shashank Kunikullaya | suk@andrew.cmu.edu
#               Vamsidhar Parasurampuram | vamsidhp@andrew.cmu.edu
#This file has the code that implements BeautifulSoup to scrape data from the given website
#This file is imported by the 'ranking_code' module

class TableScrapper:
    results = []
    
    def fetch(self, url):
        return requests.get(url)
    
    def parse(self, html):
        content = BeautifulSoup(html, 'lxml')
        table = content.find('table')
        rows = table.findAll('tr')
        self.results.append([header.text.strip() for header in rows[0].findAll('th')])
        
        for row in rows:
            self.results.append([data.text.strip() for data in row.findAll('td')])
        sum = 0
        for i in range(len(self.results)-2):
            sum+=int(self.results[i+2][2].replace(',',''))
            
    def run(self):
        response = self.fetch("https://www.homesnacks.com/safest-neighborhoods-in-pittsburgh-pa/")
        self.parse(response.text)
        
    def runAll():
        scraper = TableScrapper()
        scraper.run()
    
